from pydantic import ConfigDict, BaseModel
from sqlalchemy import String, Column, Integer, Boolean

from database import Base

class UserModel(Base):
    # model_config = ConfigDict(ignored_types=(IgnoredType,))
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    role = Column(String)
    is_active = Column(Boolean)

class UserCreateRequest(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    role: str

class UserCreateResponse(BaseModel):
    email: str
    first_name: str
    last_name: str
    id: int

class UserLoginRequest(BaseModel):
    email: str
    password: str

class UserLoginResponse(BaseModel):
    email: str
    first_name: str
    last_name: str
    id: int
    token: str


