from app import create_app
from app.config import get_settings

app = create_app(get_settings())
