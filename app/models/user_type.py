from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class UserType(Base):
    """
    SQLAlchemy model for the 'user_types' table.
    """

    __tablename__ = "user_types"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)

    # Relationships
    users = relationship("User", back_populates="user_type")
