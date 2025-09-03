from fastapi import FastAPI

from app.models.settings import Settings
from app.routers import user as user_router, centers as centers_router


def __setup_router(app: FastAPI):
    app.include_router(
        user_router.router
    )
    app.include_router(
        centers_router.router
    )

def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        description=settings.description,
    )
    __setup_router(app)
    return app
