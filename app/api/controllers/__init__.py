from fastapi import FastAPI
from .user import router as user_router


def setup(app: FastAPI) -> None:
    app.include_router(
        router=user_router,
        tags=["user"]
    )
