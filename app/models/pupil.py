from app.models.user import AccountData
from pydantic import BaseModel
from typing import List, Optional


class Pupil(BaseModel):
    user_id: str
    orphanage_id: str
    achievements: List[int] = []
    nickname: Optional[str] = None
    name: Optional[str] = None
    surname: Optional[str] = None
    patronymic: Optional[str] = None
    bio: Optional[str] = None


class PupilsInCreate(BaseModel):
    """Используется для генерации аккаунтов воспитанников
    в количестве accounts_count с привязкой к детскому 
    дому orphanage_id"""
    accounts_count: int
    orphanage_id: str


class PupilsAccountsInResponse(BaseModel):
    """Модель используется при возврате данных аккаунтов с
    роута генерации аккаунтов воспитанников"""
    accounts: List[AccountData]
