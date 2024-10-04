from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from app.config import settings

bot = Bot(token=settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


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
