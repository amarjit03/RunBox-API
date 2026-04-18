from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    #APP Config

    app_name: str = "FastAPI App"
    debug: bool = False
    port: int = 8000
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings():
    return Settings()