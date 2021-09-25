from ..database.mongodb import AsyncIOMotorClient

from ..core.config import database_name, users_collection_name
from ..models.user import UserInCreate, UserInDb, UserInLogin
from .exceptions import EntityDoesNotExist


async def create_user(conn: AsyncIOMotorClient, user: UserInCreate) -> UserInDb:
    user = UserInDb(**user.dict(), id='0')
    user.password = user.encode_password(user.password)
    result = await conn[database_name][users_collection_name].insert_one(user.dict())
    user.id = str(result.inserted_id)
    return user


async def find_user_by_email(conn: AsyncIOMotorClient, email: str) -> UserInDb:
    result = await conn[database_name][users_collection_name].find_one({'email': email})
    if result:
        return UserInDb(**result)

    raise EntityDoesNotExist()


async def is_user_exist(conn: AsyncIOMotorClient, username: str) -> bool:
    result = await conn[database_name][users_collection_name].find_one({'username': username})
    return True if result is not None else False


async def find_user_by_username(conn: AsyncIOMotorClient, username: str) -> UserInDb:
    result = await conn[database_name][users_collection_name].find_one({'username': username})
    if result:
        return UserInDb(**result)

    raise EntityDoesNotExist()
