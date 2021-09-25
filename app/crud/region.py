from typing import List
from app.models.region import Region
from ..database.mongodb import AsyncIOMotorClient

from ..core.config import database_name, regions_collection_name


async def update_regions(conn: AsyncIOMotorClient, regions: List[Region]):
    await conn[database_name][regions_collection_name].drop()
    for region in regions:
        await conn[database_name][regions_collection_name].insert_one(region.dict())
