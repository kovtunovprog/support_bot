from aiogram import types

from loader import dp
from utils.db_api.quick_commands import select_chat_messages


@dp.callback_query_handler(text="take_user")
async def take_user(call: types.CallbackQuery):
    operator_id = call.from_user.id
    await dp.bot.send_message(operator_id, 'С вами начат диалог')
    str_message = str(call.message.text)
    web_chat_id = str_message[str_message.find('[') + 1: str_message.find(']')]
    chat = await select_chat_messages(web_chat_id=web_chat_id)
    print(str(operator_id))
    for msg in chat:
        await dp.bot.send_message(operator_id, f'<b>{msg.full_name}</b>: {msg.msg}')
        await msg.update(operator_id=operator_id).apply()

    await call.message.edit_reply_markup()

