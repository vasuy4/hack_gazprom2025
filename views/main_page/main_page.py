from fastapi import APIRouter, Request, UploadFile, File
from utils.templates import templates
import shutil
import os

router = APIRouter()

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.get("/", name="home")
def index_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"image_url": None}
    )

@router.post("/uploads")
async def upload_image(request: Request, file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    image_url = f"/static/uploads/{file.filename}"
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"image_url": image_url}
    )
