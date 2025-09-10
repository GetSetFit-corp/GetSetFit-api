from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.orm import relationship
from typing import List, Optional

from database import Base


class Sys:
    created_by: str
    updated_by: str
    created_at: datetime
    updated_at: datetime


class Center(Base):
    """
    SQLAlchemy model for the 'centers' table.
    """

    __tablename__ = "centers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    address = Column(String(255))
    city = Column(String(255))
    description = Column(Text)
    images = Column(ARRAY(Text))
    provided_services = Column(JSONB)
    opening_days_timing = Column(JSONB)
    sys: Sys = Column(JSONB)

    # Foreign keys
    package_id = Column(Integer, ForeignKey("package.id"), nullable=False)
    workout_type_id = Column(Integer, ForeignKey("workout_types.id"), nullable=False)

    # Relationships
    package = relationship("Package", back_populates="centers")
    workout_type = relationship("WorkoutType", back_populates="centers")

    # Many-to-many relationships with back-references
    favourited_by_users = relationship(
        "User", secondary="favourite_venues", back_populates="favourite_centers"
    )
    check_ins = relationship("UserHistoryCheckIn", back_populates="center")


class ProvidedServiceByCenter(BaseModel):
    name: str


class OpeningDaysTimingByCenter(BaseModel):
    day_name: str
    open_at: str
    closed_at: str


class CentersRequestModel(BaseModel):
    name: str
    description: Optional[str]
    address: str
    city: str
    images: List[str]
    provided_services: List[ProvidedServiceByCenter]
    opening_days_timing: List[OpeningDaysTimingByCenter]
    package_id: int
    workout_type_id: int


class CentersResponseModel(BaseModel):
    id: int
    name: str
    description: Optional[str]
    address: str
    city: str
    images: List[str]
    provided_services: List[ProvidedServiceByCenter]
    opening_days_timing: List[OpeningDaysTimingByCenter]
