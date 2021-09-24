from fastapi import APIRouter

from .endpoints.test import router as test_router

router = APIRouter()
router.include_router(test_router)
