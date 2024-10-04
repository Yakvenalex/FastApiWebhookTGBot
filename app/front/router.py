from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from app.bot.create_bot import bot
from app.front.schemas import AppointmentData

router = APIRouter(prefix='', tags=['Фронтенд'])
templates = Jinja2Templates(directory='app/templates')


@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/forma", response_class=HTMLResponse)
async def read_root(request: Request, user_id: int = None, first_name: str = None):
    return templates.TemplateResponse("forma.html",
                                      {"request": request, "user_id": user_id, "first_name": first_name})


@router.post("/appointment", response_class=JSONResponse)
async def create_appointment(request: Request):
    # Получаем и валидируем JSON данные
    data = await request.json()
    validated_data = AppointmentData(**data)

    # Формируем сообщение для отправки пользователю
    message = (
        "🎉 <b>Ваша заявка успешно сохранена!</b>\n\n"
        "Вот данные, которые вы указали:\n"
        f"👤 <b>Имя:</b> {validated_data.name}\n"
        f"🧑‍🦰 <b>Пол:</b> {validated_data.gender}\n"
        f"💇 <b>Услуга:</b> {validated_data.service}\n"
        f"✂️ <b>Мастер:</b> {validated_data.stylist}\n"
        f"📅 <b>Дата:</b> {validated_data.appointment_date}\n"
        f"⏰ <b>Время:</b> {validated_data.appointment_time}"
    )

    # Отправляем сообщение через бота
    await bot.send_message(chat_id=validated_data.user_id, text=message)

    # Возвращаем успешный ответ
    return {"message": "success!"}
