from fastapi import Depends
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Get Set Fit"
    version: str = "v1"
    description: str = "Get Set Fit description"
    jwt_secret_key: str = ""
    jwt_algorithm: str = "HS256"

def get_settings() -> Settings:
    return Settings()