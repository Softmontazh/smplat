# -*- coding: utf-8 -*-
"""
Модель User - пользователь системы
"""

from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import BigInteger, Boolean, DateTime, Integer, String, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.enums import UserRole, UserLanguage

if TYPE_CHECKING:
    from app.models.task import Task


class User(Base):
    """Модель пользователя"""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Telegram ID (если пользователь из бота)
    telegram_id: Mapped[Optional[int]] = mapped_column(
        BigInteger, unique=True, index=True
    )

    # Email для веб-интерфейса
    email: Mapped[Optional[str]] = mapped_column(String(255), unique=True, index=True)

    # Имя и фамилия
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[Optional[str]] = mapped_column(String(100))

    # Контактные данные
    phone: Mapped[Optional[str]] = mapped_column(String(20))

    # Хеш пароля (для веб-интерфейса)
    password_hash: Mapped[Optional[str]] = mapped_column(String(255))

    # Роль пользователя
    role: Mapped[UserRole] = mapped_column(
        SqlEnum(UserRole, name="user_role_enum"), default=UserRole.CLIENT, index=True
    )

    # Язык интерфейса
    language: Mapped[UserLanguage] = mapped_column(
        SqlEnum(UserLanguage, name="user_language_enum"), default=UserLanguage.RU
    )

    # Статус
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)

    # Последний вход
    last_login: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    # Отношения
    tasks: Mapped[list["Task"]] = relationship(
        "Task", back_populates="owner", foreign_keys="Task.owner_id"
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email='{self.email}', telegram_id={self.telegram_id}, role={self.role})>"
