from aiogram import types, Router
from aiogram.filters.command import Command, CommandStart, CommandObject
from buttons.inline_buttons import inline_keybords


base_router = Router()


@base_router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer(text='Здарова', reply_markup=inline_keybords)