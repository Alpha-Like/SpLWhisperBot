from os import getenv as e
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

API_ID = e("API_ID", 13691707)
API_HASH = e("API_HASH", "2a31b117896c5c7da27c74025aa602b8")

BOT_TOKEN = e("BOT_TOKEN", None)