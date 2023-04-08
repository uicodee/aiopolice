from pydantic import Field

from app.api.schems import Base


class User(Base):

    telegram_id: int = Field(gt=0, alias='telegramId')
    full_name: str = Field(alias='fullName')
    username: str | None = Field(default=None)

