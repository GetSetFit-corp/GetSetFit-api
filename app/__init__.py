from fastapi import FastAPI

from app.models.setting import Settings
from app.routers import user as user_router, center as centers_router
from fastapi.middleware.cors import CORSMiddleware


def add_cors_middleware(app: FastAPI):
    origins = [
        "http://localhost",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def __setup_router(app: FastAPI):
    app.include_router(user_router.router)
    app.include_router(centers_router.router)


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        version=settings.version,
        description=settings.description,
    )
    __setup_router(app)
    add_cors_middleware(app)
    return app
