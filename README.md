# bot_allow_or_reject_join_request

This bot works with user requests in the Telegram channel. The bot checks whether the user is subscribed to another channel. If subscribed, the bot accepts the subscription request; if not, it rejects it.

The channel must be private, the invitation link to the channel must include an application to join. only in this case the bot will be able to work with the request.

Fast start:
1) create a configuration file ./settings/config.ini
In it, in the chapter [BOT], indicate your token =
2) create a virtual environment and activate it
3) install dependencies pip install -r requirements.txt
4) add your bot to both channels as an administrator
5) in ./variables.pi in the admin_ids_list list, enter the IDs of all notification recipients
6) run the bot python -m ./main