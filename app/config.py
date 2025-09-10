import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=os.path.join(BASE_DIR, ".env"))

    app_name: str = "GetSetFit"
    version: str = "0.1.0"
    description: str = "Testing"
    jwt_secret_key: str = ""
    jwt_algorithm: str = "HS256"
    sqlalchemy_database_uri: str = "postgresql://postgres:postgres@localhost/postgres"


def get_settings() -> Settings:
    settings = Settings()
    return settings
