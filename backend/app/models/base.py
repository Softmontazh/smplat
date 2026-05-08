# -*- coding: utf-8 -*-
"""
Базовый класс для всех ORM моделей
"""

from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    """Базовый класс для всех моделей"""

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), nullable=False, index=True
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now(), onupdate=func.now(), nullable=False
    )

    def __repr__(self):
        return f"<{self.__class__.__name__}(id={self.id})>"
