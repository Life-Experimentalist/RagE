from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

from app.api.endpoints.router import router as api_router
from app.core.env import settings

# Create directories if they don't exist
os.makedirs("app/templates", exist_ok=True)
os.makedirs("app/static", exist_ok=True)
os.makedirs("data", exist_ok=True)

app = FastAPI(title=settings.app.APP_NAME, version=settings.app.APP_VERSION)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Include API router
app.include_router(api_router, prefix="/api")


@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/docs")
async def read_docs(request: Request):
    return templates.TemplateResponse("docs.html", {"request": request})


@app.get("/health")
async def health_check():
    return {"status": "healthy", "app_name": settings.app.APP_NAME}
