from fastapi import APIRouter
from app.api.endpoints.router import router as endpoint_router

router = APIRouter()

# Include endpoint router
router.include_router(endpoint_router, prefix="/api")
