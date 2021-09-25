import datetime
from app.models.user import AccountData
from pydantic import BaseModel
from typing import List, Optional


class Event(BaseModel):
    region_id: str
    name: str
    description: str
    status: int
    created_at: datetime.datetime
    start_at: datetime.datetime
    users: List[str] = []
