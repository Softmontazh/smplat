# 🏢 Софтмонтаж - Платформа управления проектами

**Современная платформа для управления проектами проектирования, монтажа и продажи слаботочных систем**

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-Commercial-red)
![Company](https://img.shields.io/badge/company-ТОО%20Софтмонтаж-green)

## 📋 О проекте

**Софтмонтаж** — это специализированная платформа для управления проектами в сфере слаботочных систем. Система позволяет:

- 📊 Управлять проектами от планирования до завершения
- 📝 Создавать детальные технические задания
- 💰 Быстро формировать сметы и расценки
- 🤝 Взаимодействовать между подрядчиками и клиентами
- 🔔 Получать уведомления через Telegram бот
- 📈 Отслеживать статус работ в реальном времени

## 📜 Лицензия

Этот проект является коммерческим программным обеспечением ТОО "Софтмонтаж". Подробности см. в [LICENSE.md](./LICENSE.md).

## 🏗️ Архитектура проекта

```
smplat/
├── bot/                    # Telegram бот для интеграции и уведомлений
│   ├── handlers/
│   ├── services/
│   ├── database/
│   └── app.py
│
├── backend/                # REST API (FastAPI)
│   ├── app/
│   │   ├── models/         # ORM модели SQLAlchemy
│   │   ├── api/routes/     # API endpoints
│   │   ├── services/       # Бизнес-логика
│   │   ├── core/           # Конфигурация
│   │   └── db/             # Управление БД
│   ├── requirements.txt
│   └── main.py
│
├── frontend/               # Web UI (React + TypeScript)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api/
│   │   ├── store/
│   │   └── App.tsx
│   ├── package.json
│   └── vite.config.ts
│
└── MIGRATION_PLAN.md       # План миграции из qyzmeta-bot
```

## 🚀 Быстрый старт

Для подробной установки и инициализации проекта см. [INSTALLATION.md](./INSTALLATION.md).

### Требования
- **Python 3.10+** (для backend и бота)
- **Node.js 18+** (для frontend)
- **PostgreSQL 13+** (для БД)
- **Git** (для версионирования)

### 1️⃣ Клонирование и подготовка

```bash
cd smplat

# Создаем виртуальное окружение Python
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
```

### 2️⃣ Запуск Backend

```bash
cd backend

# Установка зависимостей
pip install -r requirements.txt

# Копирование .env и настройка БД
cp .env.example .env
# Отредактируйте .env с правильными данными БД

# Запуск сервера
uvicorn app.main:app --reload --port 8000
```

Backend будет доступен на `http://localhost:8000`
- API документация: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### 3️⃣ Запуск Frontend

```bash
cd frontend

# Установка зависимостей
npm install

# Копирование .env
cp .env.example .env

# Запуск dev сервера
npm run dev
```

Frontend будет доступен на `http://localhost:3000`

### 4️⃣ Запуск Telegram бота

```bash
cd bot

# Создание виртуального окружения
python -m venv venv
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Копирование .env
cp .env.example .env
# Добавьте TELEGRAM BOT TOKEN

# Запуск бота
python app.py
```

## 📚 Документация

- [Backend README](./backend/README.md) — Документация API
- [Frontend README](./frontend/README.md) — Документация веб-интерфейса
- [Bot README](./bot/README.md) — Документация Telegram бота
- [MIGRATION_PLAN.md](./MIGRATION_PLAN.md) — План миграции из qyzmeta-bot

## 🔄 Фазы разработки

### ✅ Фаза 1: Backend Scaffold (ЗАВЕРШЕНА)
- [x] Структура проекта
- [x] ORM модели (User, Project, Task, Quote)
- [x] Конфигурация FastAPI
- [x] Инициализация БД

### ⏳ Фаза 2: API endpoints (В РАБОТЕ)
- [ ] CRUD операции для всех моделей
- [ ] Аутентификация/авторизация
- [ ] Валидация данных
- [ ] Обработка ошибок

### ⏳ Фаза 3: Frontend (В РАБОТЕ)
- [ ] Основная структура React приложения
- [ ] Компоненты UI
- [ ] Интеграция с API

### ⏳ Фаза 4: Bot интеграция
- [ ] HTTP клиент для backend
- [ ] Упрощение handlers'ов
- [ ] Уведомления от backend

### ⏳ Фаза 5: Адаптация под Софтмонтаж
- [ ] Переименование понятий (JK → Project, etc)
- [ ] Специфичные функции для слаботочных систем
- [ ] Брендирование (логотип, цвета, контакты)

## 📊 Модели данных

### User (Пользователь)
- Telegram ID, Email
- ФИО, телефон
- Роль (Admin, Manager, Contractor, Client)
- Статус активности

### Project (Проект)
- Название, описание
- Адрес выполнения
- Контактные данные клиента
- Бюджет и статус

### Task (Техническая задача)
- Название, описание, категория
- Приоритет
- Медиа (фото/видео)
- Статус и видимость

### Quote (Смета)
- Сумма, НДС
- Дата истечения
- Примечания (гарантия, условия)
- Статус (draft, sent, accepted, rejected)

## 🔐 Роли и доступ

| Роль | Описание |
|------|---------|
| **Admin** | Полный доступ, управление пользователями |
| **Manager** | Управление проектами, задачами |
| **Contractor** | Просмотр и ответ на задачи, создание смет |
| **Client** | Создание задач, просмотр смет |
| **Guest** | Ограниченный доступ |

## 📱 Интеграция с Telegram

Telegram бот используется для:
- 🔔 Уведомлений о новых задачах
- 📲 Быстрого просмотра статуса
- 💬 Коммуникации между участниками
- 📸 Отправки медиа через bot

## 🔗 API endpoints (планируется)

```
GET    /api/health              — Проверка здоровья
POST   /api/users              — Создание пользователя
GET    /api/users/{id}         — Получить пользователя
POST   /api/projects           — Создать проект
GET    /api/projects/{id}      — Получить проект
POST   /api/tasks              — Создать задачу
GET    /api/tasks/{id}         — Получить задачу
POST   /api/quotes             — Создать смету
GET    /api/quotes/{id}        — Получить смету
```

## 🛠️ Технологический стек

### Backend
- **FastAPI** — веб-фреймворк
- **SQLAlchemy** — ORM для БД
- **PostgreSQL** — реляционная БД
- **Pydantic** — валидация данных
- **Alembic** — миграции БД

### Frontend
- **React 18** — UI библиотека
- **TypeScript** — типизация
- **Vite** — сборщик
- **Zustand** — управление состоянием
- **Axios** — HTTP клиент
- **Tailwind CSS** — стилизация

### Bot
- **aiogram 3** — Telegram API
- **SQLAlchemy** — ORM
- **PostgreSQL** — БД
- **asyncio** — асинхронность

## 📈 Дальнейшие улучшения

- [ ] Система оплаты (Stripe, Kaspi)
- [ ] Экспорт в PDF/Excel
- [ ] Интеграция с CRM
- [ ] Мобильное приложение
- [ ] Аналитика и отчеты
- [ ] Многоязычность (РУ, КК, EN)

## 📞 Контакты

**ТОО "Софтмонтаж"**
- 📧 Email: info@softmontazh.kz
- 🌐 Website: https://softmontazh.kz
- 📱 Telegram: https://t.me/softmontazh

## 📜 Лицензия

Коммерческая лицензия. Все права защищены © 2024-2025 ТОО "Софтмонтаж".

---

**Разработано для специализации в области слаботочных систем**
