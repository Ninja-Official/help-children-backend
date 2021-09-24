from fastapi import APIRouter

from .endpoints.test import router as test_router
from .endpoints.auth import router as auth_router

router = APIRouter()
router.include_router(test_router)
router.include_router(auth_router)
