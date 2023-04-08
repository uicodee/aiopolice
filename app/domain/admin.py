import asyncio

from app.api.dependencies.authentication import AuthProvider
from app.config import load_config
from app.dto import types
from app.infrastructure.database.dao.holder import HolderDao
from app.infrastructure.database.factory import create_pool, make_connection_string


async def create_admin():
    settings = load_config()
    name = input(">> Name: ")
    email = input(">> Email: ")
    password = input(">> Password: ")
    auth = AuthProvider(settings=settings)
    pool = create_pool(url=make_connection_string(settings=settings))
    async with pool() as session:
        dao = HolderDao(session=session)
        await dao.admin.add_admin(
            name=name,
            email=email,
            password=auth.get_password_hash(password=password),
            role=types.Role.SUPERADMIN
        )


asyncio.run(create_admin())
