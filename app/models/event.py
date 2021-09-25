import datetime

from fastapi.datastructures import UploadFile
from app.models.user import AccountData
from pydantic import BaseModel
from typing import List, Optional

class Event(BaseModel):
    _id: Optional[str]
    name: str
    consumers: str
    resources: str
    description: str
    location: str
    date: str

class EventRequestDto(BaseModel):
    name: str
    consumers: str
    resources: str
    description: str
    location: str
    date: str
    userpics: List[UploadFile]