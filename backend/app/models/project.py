# -*- coding: utf-8 -*-
"""
Модель Project - проект монтажа/проектирования
"""

from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import (
    BigInteger,
    DateTime,
    Float,
    ForeignKey,
    String,
    Text,
    Enum as SqlEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.enums import ProjectStatus

if TYPE_CHECKING:
    from app.models.task import Task
    from app.models.quote import Quote


class Project(Base):
    """Модель проекта слаботочной системы"""

    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, index=True)

    # Название проекта
    name: Mapped[str] = mapped_column(String(200), nullable=False, index=True)

    # Описание проекта
    description: Mapped[Optional[str]] = mapped_column(Text)

    # Адрес выполнения работ
    address: Mapped[Optional[str]] = mapped_column(String(300), index=True)

    # Город
    city: Mapped[Optional[str]] = mapped_column(String(100), index=True)

    # Контактное лицо клиента
    contact_name: Mapped[Optional[str]] = mapped_column(String(150))

    # Телефон клиента
    contact_phone: Mapped[Optional[str]] = mapped_column(String(20))

    # Email клиента
    contact_email: Mapped[Optional[str]] = mapped_column(String(255))

    # ID владельца проекта (клиента)
    owner_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id"), nullable=False, index=True
    )

    # Бюджет проекта
    budget: Mapped[Optional[float]] = mapped_column(Float)

    # Статус проекта
    status: Mapped[ProjectStatus] = mapped_column(
        SqlEnum(ProjectStatus, name="project_status_enum"),
        default=ProjectStatus.PLANNING,
        index=True,
    )

    # Дата начала
    start_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    # Плановая дата завершения
    planned_end_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True)
    )

    # Фактическая дата завершения
    actual_end_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    # Отношения
    owner: Mapped["User"] = relationship("User")

    tasks: Mapped[list["Task"]] = relationship(
        "Task", back_populates="project", cascade="all, delete-orphan"
    )

    quotes: Mapped[list["Quote"]] = relationship(
        "Quote", back_populates="project", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Project(id={self.id}, name='{self.name}', status={self.status})>"
