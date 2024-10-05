from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import JSONResponse
from app.api.schemas import AppointmentData
from app.bot.create_bot import bot
from app.api.dao import ApplicationDAO
from app.bot.keyboards.kbs import main_keyboard
from app.config import settings

router = APIRouter(prefix='/api', tags=['API'])


@router.post("/appointment", response_class=JSONResponse)
async def create_appointment(request: Request):
    # Получаем и валидируем JSON данные
    data = await request.json()
    validated_data = AppointmentData(**data)

    master_id, master_name = validated_data.stylist.split('_')
    service_id, service_name = validated_data.service.split('_')
    gender, gender_name = validated_data.gender.split('_')

    # Формируем сообщение для пользователя
    message = (
        f"🎉 <b>{validated_data.name}, ваша заявка успешно принята!</b>\n\n"
        "💬 <b>Информация о вашей записи:</b>\n"
        f"👤 <b>Имя клиента:</b> {validated_data.name}\n"
        f"🧑‍🦰 <b>Пол клиента:</b> {gender_name}\n"
        f"💇 <b>Услуга:</b> {service_name}\n"
        f"✂️ <b>Мастер:</b> {master_name}\n"
        f"📅 <b>Дата записи:</b> {validated_data.appointment_date}\n"
        f"⏰ <b>Время записи:</b> {validated_data.appointment_time}\n\n"
        "Спасибо за выбор нашей студии! ✨ Мы ждём вас в назначенное время."
    )

    # Сообщение администратору
    admin_message = (
        "🔔 <b>Новая запись!</b>\n\n"
        "📄 <b>Детали заявки:</b>\n"
        f"👤 Имя клиента: {validated_data.name}\n"
        f"💇 Услуга: {service_name}\n"
        f"✂️ Мастер: {master_name}\n"
        f"📅 Дата: {validated_data.appointment_date}\n"
        f"⏰ Время: {validated_data.appointment_time}\n"
        f"🧑‍🦰 Пол клиента: {gender_name}"
    )

    # Добавление заявки в базу данных
    await ApplicationDAO.add(
        user_id=validated_data.user_id,
        master_id=master_id,
        service_id=service_id,
        appointment_date=validated_data.appointment_date,
        appointment_time=validated_data.appointment_time,
        client_name=validated_data.name,
        gender=gender
    )
    kb = main_keyboard(user_id=validated_data.user_id, first_name=validated_data.name)
    # Отправка сообщений через бота
    await bot.send_message(chat_id=validated_data.user_id, text=message, reply_markup=kb)
    await bot.send_message(chat_id=settings.ADMIN_ID, text=admin_message, reply_markup=kb)

    # Возвращаем успешный ответ
    return {"message": "success!"}
