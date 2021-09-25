from pydantic import BaseModel
from typing import List, Optional


class OrphanageBase(BaseModel):
    title: str
    address: str
    info: str
    region_id: str
    description: Optional[str]
