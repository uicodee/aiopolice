import datetime

from fastapi import APIRouter, Query, Depends, HTTPException, status

from app import dto
from app.api import schems
from app.api.dependencies import dao_provider
from app.infrastructure.database.dao.holder import HolderDao

router = APIRouter(prefix="/user")


@router.get(
    path="/all",
    description="Get all users",
    response_model=list[dto.User]
)
async def get_users(dao: HolderDao = Depends(dao_provider)) -> list[dto.User]:
    return await dao.user.get_users()


@router.post(
    path="/new",
    description="Create new telegram user",
    response_model=dto.User
)
async def new_user(
        user: schems.User,
        dao: HolderDao = Depends(dao_provider)
) -> dto.User:
    if await dao.user.get_user(telegram_id=user.telegram_id) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already created"
        )
    user = await dao.user.add_user(
        telegram_id=user.telegram_id,
        full_name=user.full_name,
        username=user.username,
        status=dto.Status.REJECT
    )
    return user


@router.get(
    path="/",
    description="Get user by telegram id",
    response_model=dto.User
)
async def get_user(
        telegram_id: int = Query(gt=0)
) -> dto.User:
    return dto.User(
        id=1,
        created_at=datetime.datetime.now(),
        updated_at=datetime.datetime.now(),
        telegram_id=1234567,
        full_name="Example example",
        username="@username",
        status=dto.Status.REJECT
    )
