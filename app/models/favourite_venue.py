from sqlalchemy import Column, Integer, ForeignKey

from app.database import Base


class FavouriteVenue(Base):
    """
    Association table model for the many-to-many relationship between users and centers.
    """

    __tablename__ = "favourite_venues"
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    center_id = Column(Integer, ForeignKey("centers.id"), primary_key=True)
