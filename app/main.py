from app import create_app
from app.config import get_settings
from .database import Base, engine
app = create_app(get_settings())

@app.on_event("startup")
def on_startup():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

