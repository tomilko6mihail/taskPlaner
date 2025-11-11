from sqlalchemy import Boolean, ForeignKey, UUID, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

from app.db import Base

class User(Base):
    __tablename__ = "users"
    #Сначала пойдут основные поля, которые необходимо для работы самого сайта
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True) #типо логин будет
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    # email: Mapped[str] = mapped_column(String(), nullable=False, unique=True, index=True) #вроде как по ТЗ не нужно
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    #Это поля, которые будут отображаться в сведениях о пользователе
    fio: Mapped[str] = mapped_column(String(50), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False, default="guest")
    data_registred: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    #Здесь будут поля, необходимые для выдачи прав
    is_guest: Mapped[bool] = mapped_column(Boolean, default=True)
    is_employee: Mapped[bool] = mapped_column(Boolean, default=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)

    
