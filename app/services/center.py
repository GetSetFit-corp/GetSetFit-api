from app.repositories.center import CentersRepository
from app.models.center import Center as CenterModel, CentersRequestModel
from datetime import datetime

from app.utils.lat_long import get_lat_long


class CentersService:
    def __init__(self, centers_repository: CentersRepository):
        self.centers_repository = centers_repository

    def query(self):
        return self.centers_repository.get_centers_list()

    def insert(self, center_payload: CentersRequestModel, user):
        address = center_payload.address
        location: dict = get_lat_long(address.name)
        updated_address = {
            "name": address.name,
            "latitude": location.get("latitude"),
            "longitude": location.get("longitude"),
            "suggested_name": location.get("suggested_name"),
        }
        sys = {
            "created_by": user.get("user_id"),
            "updated_by": user.get("user_id"),
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
        }
        # Convert list of ProvidedServiceByCenter models to a list of dictionaries
        provided_services_dicts = [
            service.model_dump() for service in center_payload.provided_services
        ]

        # Convert list of OpeningDaysTimingByCenter models to a list of dictionaries
        opening_days_timing_dicts = [
            timing.model_dump() for timing in center_payload.opening_days_timing
        ]

        center_model = CenterModel(
            address=updated_address,
            city=center_payload.city,
            name=center_payload.name,
            images=center_payload.images,
            provided_services=provided_services_dicts,
            opening_days_timing=opening_days_timing_dicts,
            description=center_payload.description,
            package_id=center_payload.package_id,
            workout_type_id=center_payload.workout_type_id,
            sys=sys,
        )
        return self.centers_repository.create_center(center_model)
