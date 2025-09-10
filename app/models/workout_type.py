from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class WorkoutType(Base):
    """
    SQLAlchemy model for the 'workout_types' table.
    """

    __tablename__ = "workout_types"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

    # Relationships
    centers = relationship("Center", back_populates="workout_type")
