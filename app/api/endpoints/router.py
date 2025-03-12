from fastapi import APIRouter

from app.api.endpoints import rag

router = APIRouter()
router.include_router(rag.router, prefix="/rag", tags=["rag"])

@router.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Agentic Project!"}

# Additional routes can be added here as needed.
