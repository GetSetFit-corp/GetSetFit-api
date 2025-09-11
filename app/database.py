from typing import Any, Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from app.config import get_settings, Settings
from app.models import *

settings: Settings = get_settings()
engine = create_engine(settings.sqlalchemy_database_uri)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_database() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    except Exception as error:
        raise "Failed to connect to database"
    finally:
        db.close()
