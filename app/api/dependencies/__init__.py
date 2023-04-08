from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from app.api.dependencies.authentication import AuthProvider, get_admin
from app.api.dependencies.database import DbProvider, dao_provider
from app.api.dependencies.settings import get_settings
from app.config import load_config, Settings


def setup(
    app: FastAPI,
    pool: sessionmaker,
    settings: Settings,
):
    db_provider = DbProvider(pool=pool)
    auth_provider = AuthProvider(settings=settings)
    app.dependency_overrides[get_admin] = auth_provider.get_current_admin
    app.dependency_overrides[dao_provider] = db_provider.dao
    app.dependency_overrides[AuthProvider] = lambda: auth_provider
    app.dependency_overrides[get_settings] = load_config
