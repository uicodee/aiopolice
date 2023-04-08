from pydantic import BaseSettings


class Options(BaseSettings):

    secret: str


class DB(BaseSettings):
    host: str
    port: int
    name: str
    user: str
    password: str


class SettingsExtractor(BaseSettings):
    DB__HOST: str
    DB__PORT: int
    DB__NAME: str
    DB__USER: str
    DB__PASSWORD: str

    SECRET: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


class Settings(BaseSettings):
    db: DB
    opt: Options


def load_config() -> Settings:
    settings = SettingsExtractor()

    return Settings(
        db=DB(
            host=settings.DB__HOST,
            port=settings.DB__PORT,
            name=settings.DB__NAME,
            user=settings.DB__USER,
            password=settings.DB__PASSWORD,
        ),
        opt=Options(
            secret=settings.SECRET
        )
    )
