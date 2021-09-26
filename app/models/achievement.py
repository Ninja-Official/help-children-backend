from typing import List
from pydantic import BaseModel


class Achievement(BaseModel):
    title: str
    description: str
    for_roles: List[int]
    image: str
