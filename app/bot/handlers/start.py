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


@user_router.message(F.content_type == ContentType.WEB_APP_DATA)
async def parse_data(message: Message):
    print("=== WebApp Data Handler Triggered ===")
    print(f"Message type: {message.content_type}")
    print(f"Full message object: {message}")

    if message.web_app_data:
        print(f"Web app data present: {message.web_app_data.data}")
        try:
            data = json.loads(message.web_app_data.data)
            print(f"Parsed JSON data: {data}")
            await message.answer(f'Получены данные: {data}')
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}")
            await message.answer(f'Ошибка при разборе данных: {e}')
    else:
        print("No web app data in message")
        await message.answer('Данные отсутствуют!')


# Дополнительно можно добавить общий обработчик для отлова всех сообщений
@user_router.message()
async def catch_all(message: Message):
    print("=== Catch-all Handler Triggered ===")
    print(f"Message type: {message.content_type}")
    print(f"Full message object: {message}")
