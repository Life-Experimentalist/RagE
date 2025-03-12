import os
import pathway as pw
import argparse
from dotenv import load_dotenv


def main(data_dir: str, host: str, port: int):
    """Run the Pathway RAG pipeline."""
    print(f"Starting Pathway RAG pipeline on {host}:{port}")
    print(f"Loading documents from {data_dir}")

    # Define Pathway schemas
    class InputSchema(pw.Schema):
        query: str

    class DocumentSchema(pw.Schema):
        content: str
        metadata: dict

    # Input connector for documents (to read from data directory)
    docs = pw.io.fs.read(
        data_dir, format="json", schema=DocumentSchema, mode="streaming"
    )

    # Input connector for queries via REST API
    queries = pw.io.http.rest_connector(
        host=host,
        port=port,
        schema=InputSchema,
        path="/query",
        mode=pw.io.http.RestMode.POST,
    )

    # Embed documents
    embedded_docs = docs.select(
        content=pw.this.content,
        metadata=pw.this.metadata,
        embedding=pw.ml.embed(pw.this.content),
    )

    # Embed queries
    embedded_queries = queries.select(
        query=pw.this.query, embedding=pw.ml.embed(pw.this.query)
    )

    # Semantic search
    response = (
        embedded_queries.join(
            embedded_docs, pw.this.embedding.cosine_similarity(pw.right.embedding) > 0.7
        )
        .select(
            query=pw.this.query, content=pw.right.content, metadata=pw.right.metadata
        )
        .reduce(
            pw.this.query,
            results=pw.reducers.collect(
                {"content": pw.this.content, "metadata": pw.this.metadata}
            )
            .sort(pw.this.cosine_similarity, ascending=False)
            .limit(3),
        )
    )

    # Format response for output
    formatted = response.select(
        query=pw.this.query,
        results=pw.this.results,
        response=f"Here's information about: {pw.this.query}",
    )

    # Output via REST
    pw.io.http.rest_output(
        formatted,
        host=host,
        port=port,
        path="/response",
    )

    # Run the pipeline
    pw.run()


if __name__ == "__main__":
    # Load environment variables
    load_dotenv()

    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Run Pathway RAG pipeline")
    parser.add_argument(
        "--data-dir",
        type=str,
        default="./data",
        help="Directory containing document data",
    )
    parser.add_argument(
        "--host",
        type=str,
        default=os.environ.get("EMBEDDER_HOST", "localhost"),
        help="Host for the REST API",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("EMBEDDER_PORT", "8000")),
        help="Port for the REST API",
    )

    args = parser.parse_args()

    main(args.data_dir, args.host, args.port)
