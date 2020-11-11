from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


first_msg_button = InlineKeyboardMarkup(row_width=1)
take_user = InlineKeyboardButton(text='Начать диалог', callback_data="take_user")
first_msg_button.insert(take_user)