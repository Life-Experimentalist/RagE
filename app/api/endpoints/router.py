from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI Agentic Project!"}

# Additional routes can be added here as needed.