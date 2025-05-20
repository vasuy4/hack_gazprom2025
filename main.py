from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown

main_app = FastAPI(lifespan=lifespan)


if __name__ == '__main__':
    uvicorn.run(
        "main:main_app"
    )
