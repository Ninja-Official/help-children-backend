from ..database.mongodb import AsyncIOMotorClient

from ..core.config import database_name, users_collection_name
from ..models.user import UserInCreate, UserInDb


async def create_user(conn: AsyncIOMotorClient, user: UserInCreate) -> UserInDb:
    result = await conn[database_name][users_collection_name].insert_one(user.dict())
    return UserInDb(**user.dict())
