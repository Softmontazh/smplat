# -*- coding: utf-8 -*-
"""
Pydantic схемы для API
"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr, Field
from app.models.enums import (
    UserRole,
    UserLanguage,
    TaskStatus,
    QuoteStatus,
    ProjectStatus,
)

# ========== USER SCHEMAS ==========


class UserBase(BaseModel):
    """Базовая схема пользователя"""

    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: Optional[str] = Field(None, max_length=100)
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    language: UserLanguage = UserLanguage.RU


class UserCreate(UserBase):
    """Создание пользователя"""

    password: Optional[str] = None


class UserUpdate(BaseModel):
    """Обновление пользователя"""

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None
    language: Optional[UserLanguage] = None


class UserResponse(UserBase):
    """Ответ с данными пользователя"""

    id: int
    role: UserRole
    is_active: bool
    is_verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


# ========== TASK SCHEMAS ==========


class TaskBase(BaseModel):
    """Базовая схема задачи"""

    title: str = Field(..., min_length=5, max_length=200)
    description: str = Field(..., min_length=10)
    category: str = Field(..., max_length=100)
    priority: int = Field(default=3, ge=1, le=5)
    project_id: Optional[int] = None


class TaskCreate(TaskBase):
    """Создание задачи"""

    pass


class TaskUpdate(BaseModel):
    """Обновление задачи"""

    title: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[int] = None


class TaskResponse(TaskBase):
    """Ответ с данными задачи"""

    id: int
    owner_id: int
    status: TaskStatus
    created_at: datetime

    class Config:
        from_attributes = True


# ========== QUOTE SCHEMAS ==========


class QuoteBase(BaseModel):
    """Базовая схема сметы"""

    title: str = Field(..., min_length=5, max_length=200)
    description: Optional[str] = None
    amount: float = Field(..., gt=0)
    currency: str = Field(default="KZT", max_length=10)
    vat: Optional[float] = None
    notes: Optional[str] = None


class QuoteCreate(QuoteBase):
    """Создание сметы"""

    task_id: int
    project_id: Optional[int] = None


class QuoteUpdate(BaseModel):
    """Обновление сметы"""

    title: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    status: Optional[QuoteStatus] = None


class QuoteResponse(QuoteBase):
    """Ответ с данными сметы"""

    id: int
    uuid: str
    task_id: int
    contractor_id: int
    status: QuoteStatus
    created_at: datetime

    class Config:
        from_attributes = True


# ========== PROJECT SCHEMAS ==========


class ProjectBase(BaseModel):
    """Базовая схема проекта"""

    name: str = Field(..., min_length=5, max_length=200)
    description: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    contact_name: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[EmailStr] = None
    budget: Optional[float] = None


class ProjectCreate(ProjectBase):
    """Создание проекта"""

    pass


class ProjectUpdate(BaseModel):
    """Обновление проекта"""

    name: Optional[str] = None
    description: Optional[str] = None
    address: Optional[str] = None
    status: Optional[ProjectStatus] = None
    budget: Optional[float] = None


class ProjectResponse(ProjectBase):
    """Ответ с данными проекта"""

    id: int
    owner_id: int
    status: ProjectStatus
    created_at: datetime

    class Config:
        from_attributes = True
