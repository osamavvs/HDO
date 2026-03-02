import asyncio
from pyrogram import idle
from core.client import bot, assistant

async def main():
    await bot.start()
    await assistant.start()
    print("CristalMusic Started Successfully")
    await idle()

if __name__ == "__main__":
    asyncio.run(main())
