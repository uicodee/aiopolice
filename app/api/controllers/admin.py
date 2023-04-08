from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app import dto
from app.api.dependencies import dao_provider, AuthProvider, get_settings
from app.config import Settings
from app.infrastructure.database.dao.holder import HolderDao

router = APIRouter()


@router.post(
    path="/login"
)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        dao: HolderDao = Depends(dao_provider),
        settings: Settings = Depends(get_settings),
) -> dto.Token:
    auth = AuthProvider(settings=settings)
    admin = await auth.authenticate_admin(
        email=form_data.username,
        password=form_data.password,
        dao=dao
    )
    return auth.create_admin_token(admin=admin)
