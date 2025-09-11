from geopy import Nominatim

def get_lat_long(address_name: str):
    if not address_name:
        return None
    geolocator = Nominatim(user_agent="my_app")
    location = geolocator.geocode(address_name)
    return {
        "latitude": location.latitude,
        "longitude": location.longitude,
        "suggested_name": location.address,
    }