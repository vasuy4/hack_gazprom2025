from fastapi import APIRouter, Request

from utils.templates import templates

router = APIRouter()

@router.get("/", name="home")
def index_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
