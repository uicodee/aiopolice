from sqlalchemy import Column, BigInteger, String, Enum

from app.dto import types
from app.infrastructure.database.models.base import BaseModel


class User(BaseModel):

    __tablename__ = "user"

    telegram_id = Column(BigInteger, nullable=False)
    full_name = Column(String, nullable=False)
    username = Column(String(length=255), nullable=True)
    status = Column(Enum(types.Status), nullable=False, default=types.Status.REJECT)
    role = Column(Enum(types.Role), nullable=False, default=types.Role.USER)
