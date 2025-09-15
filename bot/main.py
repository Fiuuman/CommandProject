from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from routers.user_handlers import base_router
import asyncio
import logging

async def main():
    bot = Bot('8246245598:AAHfBQBuyxkQozOlqGNV6snTKACbcuysPMs')
    dp = Dispatcher()

    dp.include_router(base_router)

    await bot.set_my_commands(
        [BotCommand(command='start', description='Приветсвие')]
    )


    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

