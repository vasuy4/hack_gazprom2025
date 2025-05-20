from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8000

class Settings(BaseSettings):
    run: RunConfig = RunConfig()


settings = Settings()
