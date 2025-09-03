from datetime import datetime

from sqlalchemy import Column, Integer, String, JSON

from database import Base

class Sys:
    created_by: str
    updated_by: str
    created_at: datetime
    updated_at: datetime

class CentersModel(Base):
    __tablename__ = "centers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    image_gallery = Column(JSON)
    address = Column(String)
    city = Column(String)
    sys: Sys = Column(JSON)

