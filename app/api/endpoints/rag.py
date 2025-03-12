from typing import List, Optional
from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel

from app.rag.document_store import Document
from app.rag.insurance_service import insurance_service, PolicyInfo
from app.rag.indexer import indexer

router = APIRouter()


class QueryRequest(BaseModel):
    query: str
    max_results: int = 3
    policy_filter: Optional[str] = None


class DocumentInput(BaseModel):
    content: str
    source: str = "Unknown Policy"
    policy_type: Optional[str] = None


class DocumentsInput(BaseModel):
    documents: List[DocumentInput]


class QueryResponse(BaseModel):
    query: str
    response: str
    context: str
    sources: List[str]
    policy_info: Optional[dict] = None


@router.post("/query", response_model=QueryResponse)
async def query_rag(request: QueryRequest):
    """Query the insurance RAG system."""
    try:
        result = await insurance_service.query(request.query, request.max_results)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error processing insurance query: {str(e)}"
        )


@router.post("/documents")
async def add_documents(request: DocumentsInput, background_tasks: BackgroundTasks):
    """Add insurance policy documents to the RAG system."""
    try:
        documents = []
        for doc in request.documents:
            # Create document with metadata
            metadata = {"source": doc.source}
            if doc.policy_type:
                metadata["policy_type"] = doc.policy_type

            doc_obj = Document(content=doc.content, metadata=metadata)
            documents.append(doc_obj)

            # Index document in the background
            background_tasks.add_task(
                indexer.index_document, content=doc.content, metadata=metadata
            )

        # Add to in-memory store for quick access
        count = await insurance_service.add_documents(documents)
        return {
            "status": "success",
            "added": count,
            "message": "Insurance policy documents added successfully",
        }
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error adding insurance documents: {str(e)}"
        )
