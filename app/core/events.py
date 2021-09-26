from app.crud.achievement import update_achievements
from app.models.achievement import Achievement
import os
from app.crud.region import update_regions
from app.database.mongodb import get_database
from app.models.region import Region
from os import name
from ..database.mongodb_connection import connect_to_mongo, close_mongo_connection
import re
import json


async def on_start_application():
    await connect_to_mongo()

    regions_path = os.path.join(os.path.abspath(
        os.curdir), 'app/core/data/regions.txt')
    achievements_path = os.path.join(os.path.abspath(
        os.curdir), 'app/core/data/achievements.json')
    conn = await get_database()
    with open(regions_path, encoding='ISO-8859-1') as f:
        regions_lines = f.read().splitlines()
        regions = []
        for region in regions_lines:
            region_code = int(re.search(r'\d+', region).group(0))
            region_name = re.search(
                r'\|.+\|', region).group(0).replace('|', '')
            regions.append(Region(name=region_name, code=region_code))
        await update_regions(conn, regions)

    with open(achievements_path, encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        print(json_data)
        achievements = []
        for achievement in json_data['achievements']:
            achievements.append(Achievement(**achievement))

        await update_achievements(conn, achievements)


async def on_stop_application():
    await close_mongo_connection()
