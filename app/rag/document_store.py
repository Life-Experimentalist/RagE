from typing import Any, Dict, List

from pydantic import BaseModel


class Document(BaseModel):
    """Document with content and metadata."""

    content: str
    metadata: Dict[str, Any] = {}


class SimpleDocumentStore:
    """Simple in-memory document store for RAG implementation."""

    def __init__(self):
        self.documents: List[Document] = []

    def add_documents(self, documents: List[Document]):
        """Add documents to the store."""
        if not documents:
            return

        self.documents.extend(documents)

    def search(self, query: str, k: int = 3) -> List[Document]:
        """Perform a simple search for documents."""
        if not self.documents:
            return []

        # Very simple search - in real app, use embeddings/vectors
        # Just return the k documents (or all if less than k)
        return self.documents[: min(k, len(self.documents))]


# Create a global document store instance
document_store = SimpleDocumentStore()
