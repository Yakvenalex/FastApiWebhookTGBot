import json
from aiogram import Router, F
from aiogram.enums.content_type import ContentType
from aiogram.filters import CommandStart
from aiogram.types import Message

user_router = Router()


# Хендлер команды /start
@user_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"👋 Привет, <b>{message.from_user.full_name}</b>!")