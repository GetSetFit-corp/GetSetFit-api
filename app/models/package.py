from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.orm import relationship

from app.database import Base


class Package(Base):
    """
    SQLAlchemy model for the 'package' table.
    """

    __tablename__ = "package"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    allowed_check_in_per_month = Column(Integer)
    allowed_check_in_per_day = Column(Integer)

    # Relationships
    users = relationship("User", back_populates="package")
    centers = relationship("Center", back_populates="package")
