import logging

from motor.motor_asyncio import AsyncIOMotorClient
from ..core.config import MONGO_URL
from .mongodb import db


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(MONGO_URL)


async def close_mongo_connection():
    db.client.close()
