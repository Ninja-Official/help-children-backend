from typing import List
from fastapi.datastructures import UploadFile
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.crud.exceptions import EntityDoesNotExist
from ..database.mongodb import AsyncIOMotorClient
from bson.objectid import ObjectId
from ..database.mongodb import AsyncIOMotorClient
from ..core.config import database_name, events_collection_name, events_images_collection_name
from ..models.event import Event, EventRequestDto
from gridfs import GridFS
from PIL import Image 

async def create_event(conn: AsyncIOMotorClient, event: Event, image: UploadFile) -> Event:
    db = conn[database_name]
    print(image.file.readlines())
    result = await db[events_collection_name].insert_one(event.dict())
    return event
    
async def get_event_by_id(conn: AsyncIOMotorClient, event_id: str) -> EventRequestDto:
    event = await conn[database_name][events_collection_name].find_one({'event_id': ObjectId(event_id)})
    
    if event:
        return Event(**event)

    raise EntityDoesNotExist()

async def get_events(conn: AsyncIOMotorDatabase, from_id: str, ammount: int) -> List[EventRequestDto]:
    event = await conn[database_name][events_collection_name].find().sort({"event_id":from_id}).limit(ammount)
    
    if event:
        return List(**result)

    raise EntityDoesNotExist()