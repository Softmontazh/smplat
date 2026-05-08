# -*- coding: utf-8 -*-
"""
Модель Quote - смета/расценка от подрядчика
"""

import uuid
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import (
    BigInteger,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    Enum as SqlEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.enums import QuoteStatus

if TYPE_CHECKING:
    from app.models.task import Task
    from app.models.user import User
    from app.models.project import Project


class Quote(Base):
    """Модель сметы/расценки"""

    __tablename__ = "quotes"

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, index=True
    )

    # UUID для публичного доступа
    uuid: Mapped[str] = mapped_column(
        String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False
    )

    # Название сметы
    title: Mapped[str] = mapped_column(String(200), nullable=False)

    # Описание
    description: Mapped[Optional[str]] = mapped_column(Text)

    # ID задачи
    task_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tasks.id"), nullable=False, index=True
    )

    # ID проекта (может быть NULL)
    project_id: Mapped[Optional[int]] = mapped_column(
        Integer, ForeignKey("projects.id"), index=True
    )

    # ID подрядчика (автор сметы)
    contractor_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id"), nullable=False, index=True
    )

    # Сумма сметы
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    # Валюта (тенге, доллар и т.д.)
    currency: Mapped[str] = mapped_column(String(10), default="KZT")

    # НДС
    vat: Mapped[Optional[float]] = mapped_column(Float)

    # Статус сметы
    status: Mapped[QuoteStatus] = mapped_column(
        SqlEnum(QuoteStatus, name="quote_status_enum"),
        default=QuoteStatus.DRAFT,
        index=True,
    )

    # Дата истечения предложения
    expires_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    # Дата принятия
    accepted_at: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    # Примечания (условия, гарантия и т.д.)
    notes: Mapped[Optional[str]] = mapped_column(Text)

    # Отношения
    task: Mapped["Task"] = relationship(
        "Task", back_populates="quotes", foreign_keys=[task_id]
    )

    project: Mapped[Optional["Project"]] = relationship(
        "Project", back_populates="quotes", foreign_keys=[project_id]
    )

    contractor: Mapped["User"] = relationship("User", foreign_keys=[contractor_id])

    def __repr__(self) -> str:
        return f"<Quote(id={self.id}, uuid='{self.uuid}', amount={self.amount}, status={self.status})>"
