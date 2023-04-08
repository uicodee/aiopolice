from fastapi import FastAPI
from .user import router as user_router
from .admin import router as admin_router


def setup(app: FastAPI) -> None:
    app.include_router(
        router=admin_router,
        tags=["admin"]
    )
    app.include_router(
        router=user_router,
        tags=["user"]
    )
