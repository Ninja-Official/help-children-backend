import os
from app.crud.region import update_regions
from app.database.mongodb import get_database
from app.models.region import Region
from os import name
from ..database.mongodb_connection import connect_to_mongo, close_mongo_connection
import re


async def on_start_application():
    await connect_to_mongo()

    regions_path = os.path.join(os.path.abspath(
        os.curdir), 'app/core/data/regions.txt')

    with open(regions_path) as f:
        regions_lines = f.read().splitlines()
        regions = []
        for region in regions_lines:
            region_code = int(re.search(r'\d+', region).group(0))
            region_name = re.search(
                r'\|.+\|', region).group(0).replace('|', '')
            regions.append(Region(name=region_name, code=region_code))
        conn = await get_database()
        await update_regions(conn, regions)


async def on_stop_application():
    await close_mongo_connection()
