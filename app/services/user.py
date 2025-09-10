from app.repositories.user import UserRepository
from app.models import User as UserModel
from app.utils.auth import generate_hashed_password
from geopy.geocoders import Nominatim


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_lat_long(self, address_name: str):
        if not address_name:
            return None
        geolocator = Nominatim(user_agent="my_app")
        location = geolocator.geocode(address_name)
        return {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "suggested_name": location.address,
        }

    async def create_user(self, user_payload):
        address = user_payload.address
        location: dict = self.get_lat_long(address.name)
        updated_address = {
            "name": address.name,
            "latitude": location.get("latitude"),
            "longitude": location.get("longitude"),
            "suggested_name": location.get("suggested_name"),
        }
        user_payload = UserModel(
            email=user_payload.email,
            first_name=user_payload.first_name,
            last_name=user_payload.last_name,
            address=updated_address,
            phone_number=user_payload.phone_number,
            hashed_password=generate_hashed_password(user_payload.password),
            is_active=True,
            user_type_id=user_payload.user_type_id,
            package_id=user_payload.package_id,
            image=user_payload.image,
        )
        return self.user_repository.insert(user_payload)

    async def authenticate_user(self, username: str, password: str):
        return self.user_repository.get_by_username_or_email(username, password)
