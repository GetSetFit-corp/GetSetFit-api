from sqlalchemy import Column, Integer, String

from database import Base


class Category(Base):
    """
    SQLAlchemy model for the 'categories' table.
    """

    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
