from typing import List
from app.models.achievement import Achievement
from ..database.mongodb import AsyncIOMotorClient

from ..core.config import database_name, achievements_collection_name


async def update_achievements(conn: AsyncIOMotorClient, achievements: List[Achievement]):
    await conn[database_name][achievements_collection_name].drop()
    await conn[database_name][achievements_collection_name].create_index([("achievement_id", -1)])
    for achievement in achievements:
        await conn[database_name][achievements_collection_name].insert_one(achievement.dict())
