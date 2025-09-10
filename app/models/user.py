from pydantic import ConfigDict, BaseModel
from sqlalchemy import String, Column, Integer, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship

from database import Base


class AddressModel(BaseModel):
    name: str


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    address = Column(JSONB)
    phone_number = Column(String(20))
    email = Column(String(255), nullable=False, unique=True)
    image = Column(String(255))
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean)

    # Foreign keys
    user_type_id = Column(Integer, ForeignKey("user_types.id"))
    package_id = Column(Integer, ForeignKey("package.id"))

    # Relationships
    user_type = relationship("UserType", back_populates="users")
    package = relationship("Package", back_populates="users")

    # Many-to-many relationships with back-references
    favourite_centers = relationship(
        "Center", secondary="favourite_venues", back_populates="favourited_by_users"
    )
    check_ins = relationship("UserHistoryCheckIn", back_populates="user")


class UserCreateRequest(BaseModel):
    first_name: str
    last_name: str
    address: AddressModel
    phone_number: str
    email: str
    image: str
    password: str
    user_type_id: str
    package_id: int
    is_active: bool = True


class UserCreateResponse(BaseModel):
    email: str
    first_name: str
    last_name: str
    id: int


class UserLoginRequest(BaseModel):
    email: str = "lalitkushwah.dev@gmail.com"
    password: str = "kush"


class UserLoginResponse(BaseModel):
    user_id: int
    login_token: str
