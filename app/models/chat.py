from app.models.user import AccountData
from pydantic import BaseModel
from typing import List, Optional


class ChatMessage(BaseModel):
    text: str
    date: str
    user_id: str


class Chat(BaseModel):
    participants: List[str] = []
    messages: List[ChatMessage] = []
