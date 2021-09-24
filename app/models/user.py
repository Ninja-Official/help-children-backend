from typing import Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    avatar: Optional[str] = None
    role_id: int


class UserInDb(UserBase):
    password: str


class UserInLogin(BaseModel):
    email: str
    password: str


class UserInCreate(UserInLogin):
    username: str
    role_id: int
