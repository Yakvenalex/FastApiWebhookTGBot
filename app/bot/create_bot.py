from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand, BotCommandScopeDefault, WebAppInfo

from app.config import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


# Функция, которая настроит командное меню (дефолтное для всех пользователей)


async def start_bot():
    try:
        await bot.send_message(settings.ADMIN_ID, f'Я запущен🥳.')
    except:
        pass


async def stop_bot():
    try:
        await bot.send_message(settings.ADMIN_ID, 'Бот остановлен. За что?😔')
    except:
        pass
