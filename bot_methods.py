import asyncio
import random

import variables

class BotMethods:
    def __init__(self, bot_class):
        self.bot_class = bot_class

    async def chat_join_request(self, request):
        pass
        user_id = request.from_user.id
        channel_id = request.chat.id
        channel_name = request.chat.full_name
        check_channel_subscription = variables.friendly_channel_id
        the_user_is_subscribed = await self.is_subscriber(chat_id=check_channel_subscription, user_id=user_id)
        if the_user_is_subscribed:
            await self.send_message_to_admins(from_user=request.from_user, allow=True)
            await self.bot_class.bot.approve_chat_join_request(chat_id=channel_id, user_id=user_id)
        else:
            await self.send_message_to_admins(from_user=request.from_user, allow=False)
            await self.bot_class.bot.decline_chat_join_request(chat_id=channel_id, user_id=user_id)

    async def is_subscriber(self, **kwargs) -> bool:
        user_id = kwargs['user_id'] if kwargs.get('user_id') and kwargs['user_id'] else None
        chat_id = kwargs['chat_id'] if kwargs.get('chat_id') and kwargs['chat_id'] else None
        if not user_id or not chat_id:
            return False
        try:
            chat_member = await self.bot_class.bot.get_chat_member(
                chat_id=chat_id,
                user_id=user_id
            )
            if chat_member.status in ["member", "creator"]:
                return True
            else:
                return False
        except Exception as ex:
            print(ex)
            return False

    async def send_message_to_admins(self, **kwargs):
        admin_ids_list = kwargs['admin_ids_list'] if kwargs.get('admin_ids_list') else variables.admin_ids_list
        text = await self.compose_text(**kwargs)
        for admin_id in admin_ids_list:
            await self.bot_class.bot.send_message(admin_id, text, parse_mode="html")
            index = admin_ids_list.index(admin_id)
            if admin_ids_list.index(admin_id) != len(admin_ids_list):
                await asyncio.sleep(random.randrange(2, 10))

    async def compose_text(self, **kwargs) -> str:
        from_user = kwargs['from_user']
        allow = kwargs['allow']
        text = f"Поступил запрос на подписку на канал {variables.announcements_channel_name}\n" \
               f"от пользователя:\n\n" \
               f"User_id: {from_user.id}\n" \
               f"Username: {from_user.username}\n" \
               f"Full_name: {from_user.full_name}\n\n"
        text = f"✅ {text}Запрос был принят т.к. пользователь действующий подписчик на канал {variables.friendly_channel_name}" \
            if allow else f"⛔️ {text}Запрос был отклонен, т.к. пользователь не подписан на канал {variables.friendly_channel_name}"
        return text