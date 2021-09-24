from app.core.security import get_password_hash, verify_password
from pydantic import BaseModel
from typing import List, Optional


class PupilBase(BaseModel):
    username: str
    orphanage_id: str
    achievements: List[int] = []
    avatar: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    patronymic: Optional[str] = None
    bio: Optional[str] = None


class PupilInDb(PupilBase):
    password: str

    def encode_password(self, passwd: str) -> str:
        return get_password_hash(passwd)

    def check_password(self, passwd: str) -> bool:
        return verify_password(passwd, self.password)


class PupilsInCreate(BaseModel):
    orphanage_id: str
    accounts_count: int


class PupilAccount(BaseModel):
    username: str
    password: str


class PupilsAccountsInResponse(BaseModel):
    accounts: List[PupilAccount]
