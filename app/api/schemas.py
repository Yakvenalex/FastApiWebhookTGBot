from pydantic import BaseModel, Field
from datetime import date, time


# Модель для валидации данных
class AppointmentData(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Имя клиента")
    gender: str = Field(..., min_length=2, max_length=50, description="Пол клиента")
    service: str = Field(..., min_length=2, max_length=50, description="Услуга клиента")
    stylist: str = Field(..., min_length=2, max_length=50, description="Имя мастера")
    appointment_date: date = Field(..., description="Дата назначения")  # Переименовал поле
    appointment_time: time = Field(..., description="Время назначения")  # Переименовал поле
    user_id: int = Field(..., description="ID пользователя Telegram")
