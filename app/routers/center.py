from typing import List

from fastapi import APIRouter, Depends

from app.repositories.center import CentersRepository
from app.utils.auth import get_current_user
from app.database import get_database
from app.models.center import CentersResponseModel, CentersRequestModel
from app.services.center import CentersService
from sqlalchemy.orm import Session

router = APIRouter()


def get_center_repository(db: Session = Depends(get_database)) -> CentersRepository:
    return CentersRepository(db)


def get_center_service(
    repo: CentersRepository = Depends(get_center_repository),
) -> CentersService:
    return CentersService(repo)


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
