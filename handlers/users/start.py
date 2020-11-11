from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.inline import first_msg_button
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=first_msg_button)
