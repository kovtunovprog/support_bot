from aiogram import types
from aiogram.dispatcher.filters import Command

from data.config import admins
from loader import dp
from utils.db_api.quick_commands import get_web_chat_id, delete_chat_history_from_operator


dp.message_handler(Command('new_operator'), chat_id=admins)
async def new_operator(message: types.Message):
    pass