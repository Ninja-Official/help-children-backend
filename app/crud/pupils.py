from app.crud.exceptions import EntityDoesNotExist
from ..database.mongodb import AsyncIOMotorClient
from bson.objectid import ObjectId
from ..core.config import database_name, pupils_collection_name
from ..models.pupil import Pupil


async def create_pupil(conn: AsyncIOMotorClient, pupil: Pupil) -> Pupil:
    result = await conn[database_name][pupils_collection_name].insert_one(pupil.dict())
    return pupil


async def find_pupil_by_user_id(conn: AsyncIOMotorClient, user_id: str) -> Pupil:
    result = await conn[database_name][pupils_collection_name].find_one({'user_id': ObjectId(user_id)})
    
    if result:
        return Pupil(**result)

    raise EntityDoesNotExist()
