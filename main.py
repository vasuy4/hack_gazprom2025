from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from views import router as views_router
from core.config import settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown

main_app = FastAPI(lifespan=lifespan)
main_app.mount("/static", StaticFiles(directory="static"), name="static")
main_app.include_router(
    views_router,
)

if __name__ == '__main__':
    uvicorn.run(
        "main:main_app",
        host=settings.run.host,
        port=settings.run.port,
    )
