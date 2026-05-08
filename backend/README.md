# Backend для проектов Софтмонтаж

## 📋 Описание

API сервер для платформы управления проектами слаботочных систем (монтаж, проектирование, продажа).

## 🚀 Быстрый старт

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Настройка переменных окружения
```bash
cp .env.example .env
# Отредактируйте .env файл
```

### Инициализация БД
```bash
alembic upgrade head
```

### Запуск сервера
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📚 API документация

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 📁 Структура проекта

```
backend/
├── app/
│   ├── main.py              # Точка входа
│   ├── models/              # ORM модели SQLAlchemy
│   ├── schemas/             # Pydantic схемы
│   ├── services/            # Бизнес-логика
│   ├── api/
│   │   ├── routes/          # Endpoint'ы
│   │   └── dependencies.py  # Зависимости (DB session, etc)
│   ├── core/
│   │   ├── config.py        # Конфигурация
│   │   └── security.py      # Аутентификация/авторизация
│   ├── db/
│   │   ├── engine.py        # Настройка БД
│   │   └── session.py       # Session manager
│   └── utils/               # Утилиты
├── migrations/              # Alembic миграции
├── requirements.txt
├── .env.example
└── README.md
```

## 🔧 Модели данных

- **User** - пользователь системы
- **Project** - проект монтажа/проектирования
- **Task** - техническая задача/заявка
- **Quote** - смета/расценка
- **Contractor** - подрядчик/исполнитель
- **TariffPlan** - тарифный план

## 🔗 Интеграция

Бот отправляет запросы на API backend:
- `POST /api/tasks` - создание новой задачи
- `GET /api/tasks/{id}` - получение статуса
- `POST /api/notifications` - получение уведомлений

## 👤 Автор

ТОО "Софтмонтаж"
