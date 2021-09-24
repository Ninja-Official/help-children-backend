from typing import Optional
from pydantic import BaseModel
from ..core.security import verify_password, get_password_hash


class UserBase(BaseModel):
    username: str
    email: str
    avatar: Optional[str] = None
    role_id: int


class UserInDb(UserBase):
    password: str

    def encode_password(self, password: str) -> str:
        return get_password_hash(password)

    def check_password(self, password: str) -> bool:
        return verify_password(self.password, password)


class UserInLogin(BaseModel):
    email: str
    password: str


class UserInCreate(UserInLogin):
    username: str
    role_id: int


class UserInResponse(UserBase):
    token: str
