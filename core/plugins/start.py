from pyrogram import filters
from core.client import bot
from config import MUSIC_BOT_NAME, OWNER_ID

@bot.on_message(filters.command("start"))
async def start_handler(_, message):
    await message.reply_text(
        f"🎵 مرحباً بك في {MUSIC_BOT_NAME}\n\n"
        f"👨‍💻 OWNER ID: {OWNER_ID}"
    )
