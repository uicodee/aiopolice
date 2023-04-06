from fastapi import APIRouter, Query

from app import dto

router = APIRouter(prefix="/user")


@router.get(
    path="/",
    description="Get user by telegram id",
    response_model=dto.User
)
async def get_user(
        telegram_id: int = Query(gt=0)
) -> dto.User:
    return dto.User(
        telegram_id=1234567,
        full_name="Example example",
        username="@username",
        status=dto.Status.REJECT
    )
