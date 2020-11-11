import logging

from aiogram import Dispatcher

from data.config import TEH_DEP_CHANNEL_ID, SET_DEP_CHANNEL_ID, CALL_CENTER_CHANNEL_ID
from keyboards.inline.channel_keyboars import first_msg_button


async def send_first_msg(dp: Dispatcher, support_group: int, msg: str, web_chat_id: str, full_name: str = 'anonymous'):
    chat_id = 0
    if support_group == 1:
        chat_id = TEH_DEP_CHANNEL_ID
    elif support_group == 2:
        chat_id = SET_DEP_CHANNEL_ID
    elif support_group == 3:
        chat_id = CALL_CENTER_CHANNEL_ID

    if full_name is None or full_name == '':
        full_name = 'anonymous'

    message = f'{full_name}[{web_chat_id}] написал: {msg}'
    try:
        await dp.bot.send_message(chat_id, message, reply_markup=first_msg_button)
    except Exception as err:
        logging.exception(err)


async def send_message_to_operator(dp: Dispatcher, chat_id: int, msg: str, full_name: str = 'anonymous'):
    message = f'{full_name} : {msg}'
    await dp.bot.send_message(chat_id, message)