# -*- coding: utf-8 -*-
"""
Модель Task - техническая задача/заявка от клиента
"""

from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import (
    BigInteger,
    DateTime,
    ForeignKey,
    String,
    Text,
    Enum as SqlEnum,
    Integer,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.enums import TaskStatus, TaskVisibility

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.project import Project
    from app.models.quote import Quote


class Task(Base):
    """Модель технической задачи/заявки"""

    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )

    # Название задачи
    title: Mapped[str] = mapped_column(String(200), nullable=False, index=True)

    # Описание / ТЗ задачи
    description: Mapped[str] = mapped_column(Text, nullable=False)

    # Категория (например: "Проектирование", "Монтаж", "Консультация")
    category: Mapped[str] = mapped_column(String(100), nullable=False, index=True)

    # ID владельца (клиента)
    owner_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id"), nullable=False, index=True
    )

    # ID проекта (может быть NULL для одиночных задач)
    project_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("projects.id"), index=True
    )

    # Статус задачи
    status: Mapped[TaskStatus] = mapped_column(
        SqlEnum(TaskStatus, name="task_status_enum"),
        default=TaskStatus.ACTIVE,
        index=True,
    )

    # Видимость задачи
    visibility: Mapped[TaskVisibility] = mapped_column(
        SqlEnum(TaskVisibility, name="task_visibility_enum"),
        default=TaskVisibility.PUBLIC,
    )

    # Приоритет (1-5)
    priority: Mapped[int] = mapped_column(default=3)

    # ID прикрепленного медиа (фото/видео из Telegram)
    media_id: Mapped[Optional[str]] = mapped_column(String(300))

    # Дата окончания приема заявок
    expires_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True), index=True
    )

    # Отношения
    owner: Mapped["User"] = relationship(
        "User", back_populates="tasks", foreign_keys=[owner_id]
    )

    project: Mapped[Optional["Project"]] = relationship(
        "Project", back_populates="tasks", foreign_keys=[project_id]
    )

    quotes: Mapped[list["Quote"]] = relationship(
        "Quote", back_populates="task", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<Task(id={self.id}, title='{self.title}', status={self.status})>"
