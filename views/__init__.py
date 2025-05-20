from fastapi import APIRouter

from .main_page.main_page import router as main_page_router


router = APIRouter()
router.include_router(main_page_router)
