from app.dto import Status, Base


class User(Base):

    telegram_id: int
    full_name: str
    username: str | None
    status: Status
