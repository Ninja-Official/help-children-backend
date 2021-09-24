from fastapi import APIRouter

from .endpoints.test import router as test_router
from .endpoints.auth import router as auth_router
from .endpoints.pupils import router as pupils_router

router = APIRouter()
router.include_router(test_router)
router.include_router(auth_router)
router.include_router(pupils_router)
