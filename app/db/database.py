from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

async def get_database():
    client = AsyncIOMotorClient(settings.mongo_details)
    return client[settings.database_name]


