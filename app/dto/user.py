from pydantic import Field

from app.dto import Status, Base, Role


class User(Base):

    telegram_id: int = Field(alias='telegramId')
    full_name: str = Field(alias='fullName')
    username: str | None
    status: Status
    role: Role
