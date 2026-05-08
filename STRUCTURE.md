# 📂 Структура проекта Софтмонтаж

## Полный обзор файловой системы

```
smplat/
│
├── 📁 backend/                    # FastAPI REST API
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py               # Точка входа, FastAPI приложение
│   │   │
│   │   ├── models/               # ORM модели SQLAlchemy
│   │   │   ├── __init__.py
│   │   │   ├── base.py           # Базовый класс для всех моделей
│   │   │   ├── enums.py          # Перечисления (роли, статусы)
│   │   │   ├── user.py           # Модель User
│   │   │   ├── project.py        # Модель Project
│   │   │   ├── task.py           # Модель Task
│   │   │   └── quote.py          # Модель Quote
│   │   │
│   │   ├── api/
│   │   │   ├── __init__.py
│   │   │   ├── schemas.py        # Pydantic валидационные схемы
│   │   │   ├── dependencies.py   # Зависимости для DI (DB session)
│   │   │   └── routes/           # API endpoints (будут созданы)
│   │   │       ├── __init__.py
│   │   │       ├── users.py
│   │   │       ├── projects.py
│   │   │       ├── tasks.py
│   │   │       └── quotes.py
│   │   │
│   │   ├── services/             # Бизнес-логика (будет разработана)
│   │   │   ├── __init__.py
│   │   │   ├── user_service.py
│   │   │   ├── project_service.py
│   │   │   ├── task_service.py
│   │   │   └── quote_service.py
│   │   │
│   │   ├── core/                 # Конфигурация
│   │   │   ├── __init__.py
│   │   │   ├── config.py         # Настройки приложения
│   │   │   └── security.py       # Аутентификация/авторизация
│   │   │
│   │   ├── db/                   # Управление БД
│   │   │   ├── __init__.py
│   │   │   └── engine.py         # SQLAlchemy engine и session
│   │   │
│   │   └── utils/                # Утилиты
│   │       ├── __init__.py
│   │       └── helpers.py        # Вспомогательные функции
│   │
│   ├── migrations/               # Alembic миграции БД
│   │   └── versions/
│   │
│   ├── requirements.txt          # Python зависимости
│   ├── .env.example              # Пример переменных окружения
│   ├── README.md                 # README для backend
│   └── tests/                    # Тесты (планируется)
│
├── 📁 frontend/                   # React веб-интерфейс
│   ├── src/
│   │   ├── main.tsx              # Точка входа React
│   │   ├── App.tsx               # Главное приложение с маршрутами
│   │   ├── index.css             # Глобальные стили
│   │   │
│   │   ├── components/           # React компоненты
│   │   │   ├── Layout.tsx        # Макет приложения
│   │   │   ├── Navigation.tsx    # Навигационная панель
│   │   │   ├── Footer.tsx        # Подвал
│   │   │   └── ...               # Другие компоненты
│   │   │
│   │   ├── pages/                # Страницы приложения
│   │   │   ├── HomePage.tsx
│   │   │   ├── DashboardPage.tsx
│   │   │   ├── TasksPage.tsx
│   │   │   ├── ProjectsPage.tsx
│   │   │   └── QuotesPage.tsx
│   │   │
│   │   ├── api/                  # HTTP клиент
│   │   │   └── client.ts         # Axios конфигурация
│   │   │
│   │   ├── store/                # Zustand хранилище состояния
│   │   │   └── authStore.ts      # Store для аутентификации
│   │   │
│   │   ├── types/                # TypeScript типы (планируется)
│   │   │   └── index.ts
│   │   │
│   │   └── utils/                # Утилиты (планируется)
│   │       └── helpers.ts
│   │
│   ├── index.html                # HTML страница
│   ├── package.json              # Node.js зависимости
│   ├── vite.config.ts            # Vite конфигурация
│   ├── tsconfig.json             # TypeScript конфигурация
│   ├── .env.example              # Пример переменных окружения
│   ├── README.md                 # README для frontend
│   └── tailwind.config.js        # Tailwind CSS конфиг (будет)
│
├── 📁 bot/                       # Telegram бот (qyzmeta-bot)
│   ├── app.py                    # Точка входа бота
│   ├── requirements.txt          # Python зависимости
│   ├── .env.example              # Пример переменных окружения
│   │
│   ├── database/
│   │   ├── engine.py
│   │   ├── models/               # ORM модели (из qyzmeta-bot)
│   │   │   ├── model_user.py
│   │   │   ├── model_lot.py      # Task
│   │   │   ├── model_offer.py    # Quote
│   │   │   └── ...
│   │   ├── enums/
│   │   └── migrations/
│   │
│   ├── handlers/                 # Telegram handlers
│   │   ├── user_private.py
│   │   ├── admin_private.py
│   │   └── ...
│   │
│   ├── services/
│   │   ├── user_service.py
│   │   ├── lot_service.py
│   │   ├── offer_service.py
│   │   └── backend_client.py    # NEW: HTTP клиент для backend
│   │
│   ├── keyboards/                # Telegram inline keyboards
│   ├── utils/
│   ├── static/                   # Медиафайлы
│   ├── docs/                     # Документация qyzmeta
│   └── README.md
│
├── 📄 README.md                  # Главный README проекта
├── 📄 QUICKSTART.md              # Быстрый старт
├── 📄 MIGRATION_PLAN.md          # План миграции из qyzmeta-bot
├── 📄 STATUS.md                  # Статус разработки
├── 📄 DEVELOPMENT.md             # Чеклист и приоритеты
├── 📄 STRUCTURE.md               # ЭТА ФАЙЛ
├── 📄 .gitignore                 # Git ignore файл
│
├── 🔧 init.sh                    # Скрипт инициализации (Linux/Mac)
└── 🔧 init.bat                   # Скрипт инициализации (Windows)
```

## 📊 Легенда

| Символ | Значение |
|--------|----------|
| 📁 | Директория |
| 📄 | Файл |
| 🔧 | Исполняемый скрипт |
| ✅ | Созданне файлы |
| ❌ | Файлы для создания |

## 🎯 Описание основных категорий

### Backend (`backend/`)
- **Язык**: Python 3.10+
- **Фреймворк**: FastAPI
- **ORM**: SQLAlchemy
- **БД**: PostgreSQL
- **Назначение**: REST API для обработки бизнес-логики

### Frontend (`frontend/`)
- **Язык**: TypeScript
- **Фреймворк**: React 18
- **Сборщик**: Vite
- **Стили**: Tailwind CSS
- **Состояние**: Zustand
- **Назначение**: Веб-интерфейс для пользователей

### Bot (`bot/`)
- **Язык**: Python
- **Фреймворк**: aiogram 3
- **Платформа**: Telegram
- **Назначение**: Интеграция с Telegram и уведомления

## 🔄 Поток данных

```
User (Telegram)
    ↓
Bot (получает команду)
    ↓
Backend API (обрабатывает)
    ↓
Database (сохраняет)
    ↓
Frontend (отображает)
    ↓
User (видит результат)
```

## 🗂️ Содержание каждого модуля

### Backend

```
requirements.txt
├── fastapi          # Веб-фреймворк
├── sqlalchemy       # ORM
├── asyncpg          # Async PostgreSQL
├── pydantic         # Валидация
├── alembic          # Миграции БД
└── uvicorn          # ASGI сервер
```

### Frontend

```
package.json
├── react            # UI библиотека
├── react-router-dom # Маршрутизация
├── zustand          # State management
├── axios            # HTTP клиент
├── tailwindcss      # Стилизация
└── vite             # Сборщик
```

### Bot

```
requirements.txt
├── aiogram          # Telegram API
├── sqlalchemy       # ORM
├── asyncpg          # Async PostgreSQL
├── httpx            # Async HTTP клиент
└── python-dotenv    # Переменные окружения
```

## 🚀 Порядок разработки

1. **Backend API** → основная функциональность
2. **Frontend UI** → интерфейс для пользователей
3. **Bot интеграция** → уведомления и команды
4. **Адаптация** → брендирование под Софтмонтаж
5. **Тестирование** → QA и исправления
6. **Deployment** → выход в production

## 📈 Размеры проекта (примерно)

| Компонент | Файлы | Строк кода | Статус |
|-----------|-------|-----------|--------|
| Backend | 15+ | 1500+ | 40% |
| Frontend | 20+ | 1500+ | 30% |
| Bot | 40+ (qyzmeta) | 3000+ | 20% |
| **Итого** | **75+** | **6000+** | **30%** |

## 🔐 Безопасность

- JWT токены для аутентификации
- Role-based access control (RBAC)
- Валидация входных данных (Pydantic)
- CORS настройки
- Environment variables для секретов
- SQL injection защита (ORM)

## ♻️ Переиспользование кода

### Из qyzmeta-bot
- ✅ Структура database
- ✅ Логика services
- ✅ Telegram handlers
- ✅ Утилиты и хелперы

### Новое в smplat
- ✅ REST API (fastapi)
- ✅ Веб-интерфейс (React)
- ✅ Адаптация под Софтмонтаж

---

**Последнее обновление**: 8 мая 2026 г.
