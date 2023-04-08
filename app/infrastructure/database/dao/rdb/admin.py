from pydantic import parse_obj_as
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app import dto
from app.dto import types
from app.infrastructure.database.dao.rdb import BaseDAO
from app.infrastructure.database.models import Admin


class AdminDAO(BaseDAO[Admin]):
    def __init__(self, session: AsyncSession):
        super().__init__(Admin, session)

    async def add_admin(
            self,
            name: str,
            email: str,
            password: str,
            role: types.Role | None = types.Role.ADMIN
    ) -> dto.Admin:
        result = await self.session.execute(
            insert(Admin).values(
                name=name,
                email=email,
                password=password,
                role=role
            ).returning(Admin)
        )
        await self.session.commit()
        return dto.Admin.from_orm(result.scalar())

    async def get_admin(self, email: str) -> dto.Admin:
        result = await self.session.execute(
            select(Admin).filter(Admin.email == email)
        )
        admin = result.scalar()
        if admin is not None:
            return dto.Admin.from_orm(admin)

    async def get_admin_with_password(self, email: str) -> dto.PasswordAdmin:
        result = await self.session.execute(
            select(Admin).filter(Admin.email == email)
        )
        admin = result.scalar()
        if admin is not None:
            return dto.PasswordAdmin.from_orm(admin)

    async def get_admins(self) -> list[dto.Admin]:
        result = await self.session.execute(
            select(Admin).filter(Admin.role == types.Role.ADMIN)
        )
        return parse_obj_as(list[dto.Admin], result.scalars().all())
