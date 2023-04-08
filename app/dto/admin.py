from pydantic import Field

from app.dto import Base, Role


class Admin(Base):

    name: str = Field(alias='name')
    email: str
    role: Role


class PasswordAdmin(Base):

    name: str = Field(alias='name')
    email: str
    password: str
    role: Role
