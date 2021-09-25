from ..database.mongodb import AsyncIOMotorClient

from ..models.event import Event

async def create_event(conn: AsyncIOMotorClient, event: Event) -> Event:
    ...
    
