# -*- coding: utf-8 -*-
"""
Главное приложение FastAPI
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.db.engine import create_tables, drop_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Управление жизненным циклом приложения"""
    # Startup
    print("🚀 Инициализация базы данных...")
    await create_tables()
    print("✅ База данных готова")
    yield
    # Shutdown
    print("⏹️  Завершение работы...")


# Создание приложения
app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version=settings.API_VERSION,
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В production нужно ограничить
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """Главная страница API"""
    return {
        "message": "Добро пожаловать в Софтмонтаж API",
        "version": settings.API_VERSION,
        "company": settings.COMPANY_NAME,
        "docs": "/docs",
    }


@app.get("/health")
async def health():
    """Проверка здоровья сервиса"""
    return {
        "status": "ok",
        "service": "smplat-backend",
        "version": settings.API_VERSION,
    }


# TODO: Импортировать и регистрировать роутеры
# from app.api.routes import users, tasks, quotes, projects
# app.include_router(users.router)
# app.include_router(tasks.router)
# app.include_router(quotes.router)
# app.include_router(projects.router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.SERVER_HOST,
        port=settings.SERVER_PORT,
        reload=settings.DEBUG,
    )
