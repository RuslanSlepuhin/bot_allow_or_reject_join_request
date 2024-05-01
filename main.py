import asyncio

from bot_handlers import BotAllowReject
from bot_init import bot_init

async def start_bot():
    bot, dp, router, bot_name = bot_init()
    bot = BotAllowReject(bot=bot, dp=dp, router=router, bot_name=bot_name)
    await bot.read_handlers()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
