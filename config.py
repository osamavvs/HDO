import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
STRING_SESSION = os.getenv("STRING_SESSION")

MONGO_DB_URI = os.getenv("MONGO_DB_URI")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID"))
OWNER_ID = int(os.getenv("OWNER_ID"))
MUSIC_BOT_NAME = os.getenv("MUSIC_BOT_NAME", "CristalMusic")
