from pydantic import BaseModel
from datetime import datetime


class JWTMeta(BaseModel):
    expire: str
    subject: str


class JWTUser(BaseModel):
    username: str
