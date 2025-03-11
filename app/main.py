from fastapi import FastAPI

from app.api.endpoints.router import router as api_router
from app.core.env import settings

app = FastAPI(title=settings.app.APP_NAME, version=settings.app.APP_VERSION)

# Include API router
app.include_router(api_router)


@app.get("/")
async def read_root():
    return {"message": "Welcome to the Real-Time RAG App with Pathway!"}
