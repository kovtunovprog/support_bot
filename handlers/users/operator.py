import os

import requests
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api.quick_commands import get_web_chat_id, delete_chat_history_from_operator


@dp.message_handler(Command('stop_dialog'))
async def stop_dialog(message: types.Message):
    global web_chat_id
    operator_id = message.from_user.id
    msg = 'Оператор вышел из диалога'
    await delete_chat_history_from_operator(operator_id=operator_id)
    try:
        web_chat_id = await get_web_chat_id(operator_id=message.from_user.id)
        print(web_chat_id)
    except AttributeError:
        print('Оператор не подключен')
    r = requests.get('https://ngs-support-bot.herokuapp.com/api/operator', json={'web_chat_id': web_chat_id, 'msg': msg,
                                                               'connection': 'closed'})
    await message.answer(text='Вы закончили диалог')


@dp.message_handler()
async def take_messages(message: types.Message):
    global web_chat_id
    os.environ['NO_PROXY'] = '0.0.0.0'
    try:
        web_chat_id = await get_web_chat_id(operator_id=message.from_user.id)
    except AttributeError:
        print('Оператор не подключен')
    r = requests.get('https://ngs-support-bot.herokuapp.com/api/operator', json={'web_chat_id': web_chat_id, 'msg': message.text,
                                                               'connection': 'working'})
