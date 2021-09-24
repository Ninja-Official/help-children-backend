from pydantic import BaseModel
from datetime import datetime


class JWTMeta(BaseModel):
    expire: datetime
    subject: str


class JWTUser(BaseModel):
    username: str
