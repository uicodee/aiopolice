from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.dto import types
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import User


class UserDAO(BaseDAO[User]):
    def __init__(self, session: AsyncSession):
        super().__init__(User, session)

    async def add_user(
            self,
            telegram_id: int,
            full_name: str,
            username: str,
            status: types.Status
    ) -> dto.User:
        result = await self.session.execute(
            insert(User).values(
                telegram_id=telegram_id,
                full_name=full_name,
                username=username,
                status=status
            ).returning(User)
        )
        await self.session.commit()
        return dto.User.from_orm(result.scalar())

    async def get_user(self, telegram_id: int) -> dto.User:
        result = await self.session.execute(
            select(User).filter(User.telegram_id == telegram_id)
        )
        user = result.scalar()
        if user is not None:
            return dto.User.from_orm(user)
