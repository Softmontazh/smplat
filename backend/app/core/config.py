import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Конфигурация приложения"""

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost:5432/smplat"

    # API
    API_TITLE: str = "Софтмонтаж API"
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "API для платформы управления проектами слаботочных систем"
    DEBUG: bool = False

    # Server
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000

    # JWT
    SECRET_KEY: str = "change-me-in-production-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Telegram Bot Integration
    TELEGRAM_BOT_TOKEN: Optional[str] = None
    TELEGRAM_BOT_WEBHOOK_URL: Optional[str] = None

    # Корпоративная информация
    COMPANY_NAME: str = "ТОО Софтмонтаж"
    COMPANY_WEBSITE: str = "https://softmontazh.kz"
    COMPANY_PHONE: str = "+7 (___) ___-__-__"
    COMPANY_EMAIL: str = "info@softmontazh.kz"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
