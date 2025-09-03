from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from jose import jwt

from app.config import Settings, get_settings

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

security_scheme = HTTPBearer()

def generate_hashed_password(password: str) -> str:
    return bcrypt_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, app_settings: Settings, expires_delta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, app_settings.jwt_secret_key, algorithm=app_settings.jwt_algorithm)
    return encoded_jwt

def get_current_user(app_settings: Settings = Depends(get_settings), credentials: HTTPAuthorizationCredentials = Depends(security_scheme)) -> dict:
    token = credentials.credentials
    decoded_token = jwt.decode(token, app_settings.jwt_secret_key, algorithms=[app_settings.jwt_algorithm])
    if not decoded_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {
        "user_id": decoded_token.get("id"),
        "email": decoded_token.get("email")
    }