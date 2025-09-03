from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.repositories.centers import CentersRepository
from app.utils.auth import get_current_user
from database import get_database
from app.models.center import CentersModel
from app.services.centers import CentersService
from sqlalchemy.orm import Session

router = APIRouter()

def get_center_repository(db: Session = Depends(get_database)) -> CentersRepository:
    return CentersRepository(db)

def get_center_service(
    repo: CentersRepository = Depends(get_center_repository),
) -> CentersService:
    return CentersService(repo)

class CentersRequestModel(BaseModel):
    address: str
    city: str
    name: str
    image_gallery: List[str]

class CentersResponseModel(BaseModel):
    id: int
    name: str
    address: str
    city: str
    image_gallery: List[str]

@router.get('/center-list', response_model=List[CentersResponseModel], dependencies=[Depends(get_current_user)])
def get_centers(centers_service: CentersService=Depends(get_center_service)):
    return centers_service.query()

@router.post('/center', response_model=CentersResponseModel, dependencies=[Depends(get_current_user)])
def create_center(center_payload: CentersRequestModel, centers_service: CentersService=Depends(get_center_service), user = Depends(get_current_user)):
    sys = {
        "created_by": user.get("user_id"),
        "updated_by": user.get("user_id"),
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }
    center_model = CentersModel(
        address=center_payload.address,
        city=center_payload.city,
        name=center_payload.name,
        image_gallery= center_payload.image_gallery,
        sys=sys
    )
    created_center = centers_service.insert(center_model)
    return created_center



