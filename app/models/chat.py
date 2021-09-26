from pydantic import BaseModel
from typing import List, Optional
import datetime


class ChatMessage(BaseModel):
    text: str
    date: datetime.datetime
    user_id: str


class ChatMessageInCreate(ChatMessage):
    chat_id: str


class Chat(BaseModel):
    participants: List[str] = []
    messages: List[ChatMessage] = []


class ChatInDb(Chat):
    id: str


class ChatAddParticipant(BaseModel):
    chat_id: str
    user_id: str
