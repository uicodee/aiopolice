from datetime import timedelta, datetime

import pytz
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext

from app import dto
from app.api.dependencies.database import dao_provider
from app.config import Settings
from app.infrastructure.database.dao.holder import HolderDao

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def get_admin(token: str = Depends(oauth2_scheme)) -> dto.Admin:
    raise NotImplementedError


class AuthProvider:

    def __init__(self, settings: Settings):
        self.settings = settings
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.secret_key = settings.opt.secret
        self.algorythm = "HS256"
        self.access_token_expire = timedelta(days=3)

    def verify_password(
            self,
            plain_password: str,
            hashed_password: str,
    ) -> bool:
        return self.pwd_context.verify(
            plain_password,
            hashed_password,
        )

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    async def authenticate_admin(
            self,
            email: str,
            password: str,
            dao: HolderDao
    ) -> dto.Admin:
        http_status_401 = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        admin = await dao.admin.get_admin_with_password(email=email)
        if admin is None:
            raise http_status_401
        if not self.verify_password(
                password,
                admin.password,
        ):
            raise http_status_401
        return admin

    def create_access_token(
            self,
            data: dict,
            expires_delta: timedelta,
    ) -> dto.Token:
        to_encode = data.copy()
        expire = datetime.now(tz=pytz.timezone('Asia/Tashkent')) + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            self.secret_key,
            algorithm=self.algorythm,
        )
        return dto.Token(
            access_token=encoded_jwt,
            type="bearer",
        )

    def create_admin_token(
            self,
            admin: dto.Admin
    ) -> dto.Token:
        return self.create_access_token(
            data={
                "sub": admin.email
            },
            expires_delta=self.access_token_expire,
        )

    async def get_current_admin(
            self,
            token: str = Depends(oauth2_scheme),
            dao: HolderDao = Depends(dao_provider),
    ) -> dto.Admin:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(
                token,
                self.secret_key,
                algorithms=[self.algorythm],
            )
            email: str = payload.get("sub")
            if email is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        admin = await dao.admin.get_admin(email=email)
        if admin is None:
            raise credentials_exception
        return admin
