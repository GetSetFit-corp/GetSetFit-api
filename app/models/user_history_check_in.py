from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship

from database import Base


class UserHistoryCheckIn(Base):
    """
    SQLAlchemy model for the 'user_history_check_ins' table.
    """

    __tablename__ = "user_history_check_ins"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    center_id = Column(Integer, ForeignKey("centers.id"), primary_key=True)
    checked_in_at = Column(TIMESTAMP, nullable=False)

    # Relationships
    user = relationship("User", back_populates="check_ins")
    center = relationship("Center", back_populates="check_ins")
