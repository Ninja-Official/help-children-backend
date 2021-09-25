from typing import Optional
from pydantic import BaseModel
from ..core.security import verify_password, get_password_hash


class UserBase(BaseModel):
    """Базовый тип для учётных записей"""
    username: str
    email: Optional[str] = None
    avatar: Optional[str] = None
    role_id: int


class UserInDb(UserBase):
    id: str
    password: str

    def encode_password(self, passwd: str) -> str:
        return get_password_hash(passwd)

    def check_password(self, passwd: str) -> bool:
        return verify_password(passwd, self.password)


class UserInLogin(BaseModel):
    email: str
    password: str


class UserInCreate(UserInLogin):
    username: str
    role_id: int


class UserInResponse(UserBase):
    token: str


class AccountData(BaseModel):
    username: str
    password: str
