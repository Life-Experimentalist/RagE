from typing import List
from app.rag.document_store import Document, document_store


class RAGService:
    """Service for RAG operations."""

    async def query(self, user_query: str, max_docs: int = 3) -> dict:
        """Process a query through the RAG pipeline."""
        # Step 1: Retrieve relevant documents
        retrieved_docs = document_store.search(user_query, k=max_docs)

        # Step 2: Format context from retrieved documents
        context = "\n\n".join([doc.content for doc in retrieved_docs])

        # Step 3: Format sources for citation
        sources = [doc.metadata.get("source", "Unknown") for doc in retrieved_docs]

        # Step 4: In a real implementation, you would call an LLM API here
        # For simplicity, we'll just return the retrieved information
        response = {
            "query": user_query,
            "response": f"Here's information about: {user_query}",
            "context": context,
            "sources": sources,
        }

        return response

    async def add_documents(self, documents: List[Document]) -> int:
        """Add documents to the document store."""
        document_store.add_documents(documents)
        return len(documents)


# Create a global RAG service instance
rag_service = RAGService()
