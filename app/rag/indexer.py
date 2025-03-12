import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class DocumentChunk(BaseModel):
    """A chunk of text from a document."""

    content: str
    metadata: Dict[str, Any] = {}


class PathwayIndexer:
    """Indexes documents for the Pathway RAG pipeline."""

    def __init__(self, data_dir: str = "data"):
        self.data_dir = data_dir
        self._ensure_data_dir()

    def _ensure_data_dir(self):
        """Ensure the data directory exists."""
        os.makedirs(self.data_dir, exist_ok=True)

    async def index_document(
        self, content: str, metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """Index a document by chunking and saving."""
        if metadata is None:
            metadata = {}

        # Simple chunking - in a real application, use more sophisticated methods
        chunks = self._chunk_text(content)

        # Create document ID
        doc_id = f"doc_{len(os.listdir(self.data_dir)) + 1}"

        # Create chunks with metadata
        document_chunks = []
        for i, chunk in enumerate(chunks):
            chunk_metadata = metadata.copy()
            chunk_metadata.update({"document_id": doc_id, "chunk_id": i})
            document_chunks.append(
                DocumentChunk(content=chunk, metadata=chunk_metadata)
            )

        # Save document chunks
        self._save_chunks(doc_id, document_chunks)

        return doc_id

    def _chunk_text(self, text: str, chunk_size: int = 500) -> List[str]:
        """Split text into chunks of roughly equal size."""
        if len(text) <= chunk_size:
            return [text]

        chunks = []
        current_chunk = ""
        for paragraph in text.split("\n"):
            if len(current_chunk) + len(paragraph) > chunk_size:
                chunks.append(current_chunk.strip())
                current_chunk = paragraph
            else:
                current_chunk += " " + paragraph

        if current_chunk:
            chunks.append(current_chunk.strip())

        return chunks

    def _save_chunks(self, doc_id: str, chunks: List[DocumentChunk]):
        """Save document chunks to disk."""
        chunks_file = Path(self.data_dir) / f"{doc_id}.json"

        with open(chunks_file, "w") as f:
            json.dump([chunk.dict() for chunk in chunks], f)


# Create global indexer instance
indexer = PathwayIndexer()
