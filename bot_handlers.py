from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.types import ChatJoinRequest
from bot_methods import BotMethods

class BotAllowReject:
    def __init__(self, **kwargs):
        self.bot = kwargs['bot']
        self.dp = kwargs['dp']
        self.router = kwargs['router']
        self.bot_name = kwargs['bot_name']
        self.step = 1
        self.router = Router(name=__name__)
        self.join_success = False
        self.bot_methods = BotMethods(self)

    async def read_handlers(self):

        print(self.bot_name)

        @self.dp.chat_join_request()
        async def chat_join_request_handler(request: ChatJoinRequest):
            await self.bot_methods.chat_join_request(request)

        @self.dp.message(CommandStart())
        async def start(message: types.Message):
            await self.bot.send_message(message.chat.id, f"{message.chat.id}\nI'm at work")

        await self.dp.start_polling(self.bot)

