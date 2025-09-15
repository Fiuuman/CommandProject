from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo


menu = [
    [InlineKeyboardButton(text='Mini App', url='https://habr.com')]
]

inline_keybords = InlineKeyboardMarkup(inline_keyboard=menu)