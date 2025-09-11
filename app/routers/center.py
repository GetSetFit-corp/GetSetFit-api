import json
from typing import List

from fastapi import APIRouter, Depends, HTTPException

from app.repositories.center import CentersRepository
from app.repositories.user import UserRepository
from app.services.user import UserService
from app.utils.auth import get_current_user
from app.database import get_database
from app.utils.haversine_util import haversine
from app.models.center import CentersResponseModel, CentersRequestModel, NearbySearchRequest
from app.services.center import CentersService
from sqlalchemy.orm import Session

router = APIRouter()


def get_center_repository(db: Session = Depends(get_database)) -> CentersRepository:
    return CentersRepository(db)


def get_center_service(
    repo: CentersRepository = Depends(get_center_repository),
) -> CentersService:
    return CentersService(repo)

def get_user_repository(db: Session = Depends(get_database)) -> UserRepository:
    return UserRepository(db)

def get_user_service(
        repo: UserRepository = Depends(get_user_repository),
) -> UserService:
    return UserService(repo)

@router.get(
    "/center-list",
    response_model=List[CentersResponseModel],
    dependencies=[Depends(get_current_user)],
)
def get_centers(centers_service: CentersService = Depends(get_center_service)):
    return centers_service.query()


@router.post(
    "/center",
    response_model=CentersResponseModel,
    dependencies=[Depends(get_current_user)],
)
def create_center(
    center_payload: CentersRequestModel,
    centers_service: CentersService = Depends(get_center_service),
    user=Depends(get_current_user),
):
    return centers_service.insert(center_payload, user)

@router.post("/nearby-centers", response_model=List[CentersResponseModel])
async def find_nearby_centers(
        nearby_search_request: NearbySearchRequest,
        centers_service: CentersService = Depends(get_center_service),
        user_service: UserService = Depends(get_user_service),
        user: dict = Depends(get_current_user)
):
    user_id = user.get("user_id")
    current_user = await user_service.get_user_by_id(user_id)

    if not current_user:
        raise HTTPException(status_code=404,detail="User not found")
    current_user_address = current_user.address
    user_latitude = current_user_address['latitude']
    user_longitude = current_user_address['longitude']
    centers_list = centers_service.query()
    nearby_centers = []

    for center in centers_list:
        center_address = center.address
        center_latitude =center_address['latitude']
        center_longitude = center_address['longitude']

        if center_latitude is None or center_longitude is None:
            continue
        distance = haversine(
            lat1=user_latitude,
            lon1=user_longitude,
            lat2=center_latitude,
            lon2=center_longitude
        )
        if distance <= nearby_search_request.search_range_km:
            nearby_centers.append(center)


    return nearby_centers