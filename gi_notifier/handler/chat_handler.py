from telegram import Update
from telegram.ext import ContextTypes

from .. import config
from ..file import load_data, save_data


async def addition(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_member = update.my_chat_member

    if chat_member.new_chat_member.status in ["member", "administrator"]:
        added_by_user_id = str(chat_member.from_user.id)
        data = load_data()

        if added_by_user_id not in data:
            data[added_by_user_id] = {
                "user_id": chat_member.from_user.id,
                "chat_bot_id": None,
                "group_bot_id": [chat_member.chat.id],
            }
        else:
            groups = data[added_by_user_id].setdefault("group_bot_id", [])
            if chat_member.chat.id not in groups:
                groups.append(chat_member.chat.id)

        save_data(data)

        await context.bot.send_message(
            chat_id=chat_member.chat.id,
            text="Hello! I'm now part of this group."
        )
        config.logger.debug(f"Bot added to chat: {chat_member.chat.title}, id:{chat_member.chat.id}")  #noqa: E501

    elif chat_member.new_chat_member.status == "left":
        config.logger.debug(f"Bot removed from chat: {chat_member.chat.title}, id:{chat_member.chat.id}")  #noqa: E501
