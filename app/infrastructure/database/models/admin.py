from sqlalchemy import Column, BigInteger, String, Enum

from app.dto import types
from app.infrastructure.database.models.base import BaseModel


class Admin(BaseModel):

    __tablename__ = "admin"

    telegram_id = Column(BigInteger, nullable=False)
    name = Column(String, nullable=False)
    email = Column(String(length=255), nullable=True)
    password = Column(String(length=255), nullable=True)
    role = Column(Enum(types.Role), nullable=False, default=types.Role.ADMIN)
