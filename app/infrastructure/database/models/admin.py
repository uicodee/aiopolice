from sqlalchemy import Column, String, Enum

from app.dto import types
from app.infrastructure.database.models.base import BaseModel


class Admin(BaseModel):

    __tablename__ = "admin"

    name = Column(String, nullable=False)
    email = Column(String(length=255), nullable=True)
    password = Column(String(length=255), nullable=True)
    role = Column(Enum(types.Role), nullable=False, default=types.Role.ADMIN)
