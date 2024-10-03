from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

user_router = Router()


# Хендлер команды /start и кнопки "🏚 Главная"
@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привет, {message.from_user.full_name}!\n\n"
        f"К сожалению, у тебя нет доступа к функционалу этого бота. "
        f"Если это ошибка, сообщи администрации свой Telegram ID: {message.from_user.id}. "
        f"Возможно, тебе дадут доступ. Но это не точно. 🤷‍♂️")