from sqlalchemy import String, BigInteger, Integer, Date, Time, ForeignKey, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base
import enum


class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger,
                                             primary_key=True)  # Уникальный идентификатор пользователя в Telegram
    first_name: Mapped[str] = mapped_column(String, nullable=False)  # Имя пользователя
    username: Mapped[str] = mapped_column(String, nullable=True)  # Telegram username

    # Связь с заявками (один пользователь может иметь несколько заявок)
    applications: Mapped[list["Application"]] = relationship(back_populates="user")


class Master(Base):
    __tablename__ = 'masters'

    master_id: Mapped[int] = mapped_column(Integer, primary_key=True,
                                           autoincrement=True)  # Уникальный идентификатор мастера
    master_name: Mapped[str] = mapped_column(String, nullable=False)  # Имя мастера

    # Связь с заявками (один мастер может иметь несколько заявок)
    applications: Mapped[list["Application"]] = relationship(back_populates="master")


class Service(Base):
    __tablename__ = 'services'

    service_id: Mapped[int] = mapped_column(Integer, primary_key=True,
                                            autoincrement=True)  # Уникальный идентификатор услуги
    service_name: Mapped[str] = mapped_column(String, nullable=False)  # Название услуги

    # Связь с заявками (одна услуга может быть частью нескольких заявок)
    applications: Mapped[list["Application"]] = relationship(back_populates="service")


class Application(Base):
    __tablename__ = 'applications'

    class GenderEnum(enum.Enum):
        male = "Мужской"
        female = "Женский"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор заявки
    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.telegram_id'))  # Внешний ключ на пользователя
    master_id: Mapped[int] = mapped_column(Integer, ForeignKey('masters.master_id'))  # Внешний ключ на мастера
    service_id: Mapped[int] = mapped_column(Integer, ForeignKey('services.service_id'))  # Внешний ключ на услугу
    appointment_date: Mapped[Date] = mapped_column(Date, nullable=False)  # Дата заявки
    appointment_time: Mapped[Time] = mapped_column(Time, nullable=False)  # Время заявки
    gender: Mapped[GenderEnum] = mapped_column(Enum(GenderEnum), nullable=False)
    client_name: Mapped[str] = mapped_column(String, nullable=False)  # Имя пользователя
    # Связи с пользователем, мастером и услугой
    user: Mapped["User"] = relationship(back_populates="applications")
    master: Mapped["Master"] = relationship(back_populates="applications")
    service: Mapped["Service"] = relationship(back_populates="applications")