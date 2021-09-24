from ..database.mongodb import AsyncIOMotorClient

from ..core.config import database_name, users_collection_name
from ..models.user import UserInCreate, UserInDb, UserInLogin
from .exceptions import EntityDoesNotExist


async def create_user(conn: AsyncIOMotorClient, user: UserInCreate) -> UserInDb:
    user = UserInDb(**user.dict())
    user.password = user.encode_password(user.password)
    result = await conn[database_name][users_collection_name].insert_one(user.dict())
    return UserInDb(**user.dict())

async def find_user_by_email(conn: AsyncIOMotorClient, email: str) -> UserInDb:
    result = await conn[database_name][users_collection_name].find_one({'email': email})
    if result:
        return UserInDb(**result)
    
    raise EntityDoesNotExist()
