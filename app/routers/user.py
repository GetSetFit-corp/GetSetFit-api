from http import HTTPStatus
from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from app.config import get_settings, Settings
from app.repositories.user import UserRepository
from app.utils.auth import create_access_token
from app.database import get_database
from app.models.user import (
    UserCreateResponse,
    UserCreateRequest,
    UserLoginResponse,
    UserLoginRequest,
)

from app.services.user import UserService

router = APIRouter()


def get_user_repository(db: Session = Depends(get_database)) -> UserRepository:
    return UserRepository(db)


def get_user_service(
    repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repo)


oauth2_scheme = HTTPBearer()


@router.post(
    "/create_user", status_code=HTTPStatus.CREATED, response_model=UserCreateResponse
)
async def create_user(
    user_payload: UserCreateRequest, service: UserService = Depends(get_user_service)
):
    created_user = await service.create_user(user_payload)
    return UserCreateResponse(
        email=created_user.email,
        first_name=created_user.first_name,
        last_name=created_user.last_name,
        id=created_user.id,
    )


@router.post(
    "/login",
    status_code=HTTPStatus.OK,
    response_model=UserLoginResponse,
    tags=["authentication"],
)
async def login(
    form_data: UserLoginRequest,
    service: UserService = Depends(get_user_service),
    app_settings: Settings = Depends(get_settings),
):
    user_response = await service.authenticate_user(form_data.email, form_data.password)
    if not user_response:
        raise HTTPException(status_code=404, detail="Incorrect username or password")
    token = create_access_token(
        data={"id": user_response.id, "email": user_response.email},
        expires_delta=timedelta(minutes=60),
        app_settings=app_settings,
    )
    return UserLoginResponse(login_token=token, user_id=user_response.id)
