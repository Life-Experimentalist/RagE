from typing import List
from app.rag.document_store import Document, SimpleDocumentStore


class PathwayRAGService:
    """RAG service implementation using a simplified approach."""

    def __init__(self):
        self.document_store = SimpleDocumentStore()

    async def query(self, user_query: str, max_docs: int = 3) -> dict:
        """Process a query through the RAG pipeline."""
        # Get documents from the store
        retrieved_docs = self.document_store.search(user_query, k=max_docs)

        if not retrieved_docs:
            return {
                "query": user_query,
                "response": "I don't have any documents to search through yet. Please add some documents first.",
                "context": "",
                "sources": [],
            }

        # Simple simulated response
        context = "\n".join([doc.content[:100] + "..." for doc in retrieved_docs])
        sources = [doc.metadata.get("source", "Unknown") for doc in retrieved_docs]

        return {
            "query": user_query,
            "response": f"Here's information about: {user_query}",
            "context": context,
            "sources": sources,
        }

    async def add_documents(self, documents: List[Document]) -> int:
        """Add documents to the document store."""
        self.document_store.add_documents(documents)
        return len(documents)


# Create a global RAG service instance
rag_service = PathwayRAGService()
