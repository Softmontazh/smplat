# -*- coding: utf-8 -*-
"""
Перечисления для моделей
"""

from enum import Enum


class UserRole(str, Enum):
    """Роли пользователей"""

    ADMIN = "admin"
    MANAGER = "manager"
    CONTRACTOR = "contractor"  # Подрядчик/Исполнитель
    CLIENT = "client"  # Клиент
    GUEST = "guest"


class TaskStatus(str, Enum):
    """Статусы задач/заявок"""

    DRAFT = "draft"  # Черновик
    ACTIVE = "active"  # Активна
    IN_PROGRESS = "in_progress"  # В работе
    COMPLETED = "completed"  # Завершена
    CANCELLED = "cancelled"  # Отменена
    ARCHIVED = "archived"  # В архиве


class TaskVisibility(str, Enum):
    """Видимость задач"""

    PRIVATE = "private"  # Только для клиента
    INTERNAL = "internal"  # Для подрядчиков/менеджеров
    PUBLIC = "public"  # Для всех


class QuoteStatus(str, Enum):
    """Статусы смет/расчетов"""

    DRAFT = "draft"  # Черновик
    SENT = "sent"  # Отправлена клиенту
    ACCEPTED = "accepted"  # Принята
    REJECTED = "rejected"  # Отклонена
    EXPIRED = "expired"  # Истекла


class ProjectStatus(str, Enum):
    """Статусы проектов"""

    PLANNING = "planning"  # Планирование
    IN_PROGRESS = "in_progress"  # В разработке
    COMPLETED = "completed"  # Завершен
    ARCHIVED = "archived"  # В архиве


class UserLanguage(str, Enum):
    """Языки интерфейса"""

    RU = "ru"
    KK = "kk"
    EN = "en"
