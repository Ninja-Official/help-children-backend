from ..database.mongodb import AsyncIOMotorClient

from ..core.config import database_name, pupils_collection_name
from ..models.pupil import PupilInDb


async def create_pupil(conn: AsyncIOMotorClient, pupil: PupilInDb) -> PupilInDb:
    pupil.password = pupil.encode_password(pupil.password)
    result = await conn[database_name][pupils_collection_name].insert_one(pupil.dict())
    return pupil


async def is_pupil_exist(conn: AsyncIOMotorClient, username: str) -> bool:
    result = await conn[database_name][pupils_collection_name].find_one({'username': username})
    return True if result is not None else False
