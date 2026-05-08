# Установка и инициализация проекта smplat

## � Лицензия

Этот проект является коммерческим программным обеспечением ТОО "Софтмонтаж". Подробности см. в [LICENSE.md](./LICENSE.md).

## �📌 Что установлено

В проекте используются отдельные окружения для каждой подсистемы:

- `backend/` — Python API на FastAPI
- `frontend/` — React + TypeScript приложение
- `bot/` — Telegram бот на aiogram

## ✅ Общие требования

- Python 3.10 или выше
- Node.js 18 или выше
- PostgreSQL 13 или выше
- Git

## 🪟 Установка на Windows

### 1. Node.js

Если `npm` не найден, установите Node.js:

```powershell
winget install OpenJS.NodeJS.LTS --accept-source-agreements --accept-package-agreements
```

Если `npm` не обнаружился сразу, перезапустите терминал или добавьте `C:\Program Files\nodejs` в PATH.

### 2. Инициализация проекта

В корне проекта выполните:

```powershell
init.bat
```

## 🐧 Установка на Ubuntu 22.04 / VPS

### 1. Системные зависимости

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip build-essential curl git
```

### 2. Установка PostgreSQL

```bash
sudo apt install -y postgresql postgresql-contrib libpq-dev
```

### 3. Установка Node.js и npm

Для стабильной версии Node.js используйте официальный репозиторий:

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs
```

Проверьте установку:

```bash
node --version
npm --version
```

### 4. Настройка базы данных PostgreSQL

Создайте пользователя и базу данных для проекта:

```bash
sudo -u postgres createuser -P smplat_user
sudo -u postgres createdb -O smplat_user smplat
```

Если используете отдельную БД для бота, создайте вторую:

```bash
sudo -u postgres createdb -O smplat_user smplat_bot
```

### 5. Клонирование репозитория и запуск инициализации

```bash
git clone <репозиторий> smplat
cd smplat
chmod +x init.sh
./init.sh
```

### 6. Редактирование `.env`

После `init.sh` отредактируйте переменные окружения в:

- `backend/.env`
- `bot/.env`
- `frontend/.env`

Пример строки в `backend/.env` и `bot/.env`:

```env
DATABASE_URL=postgresql+asyncpg://smplat_user:<пароль>@localhost:5432/smplat
```

Для `frontend/.env`:

```env
VITE_API_URL=http://localhost:8000/api
```

### 7. Запуск сервиса после инициализации

#### Backend

```bash
cd backend
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend

```bash
cd frontend
npm run dev
```

#### Bot

```bash
cd bot
source venv/bin/activate
python app.py
```

### 8. Если `npm install` не проходит

```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

Если `node` или `npm` не доступны, пересмотрите установку Node.js и перезапустите терминал.

### 9. База данных и права

Если нужно дать доступ PostgreSQL только для пользователя, проверьте:

```bash
sudo -u postgres psql
# затем внутри psql
\du
\l
``` 

> `init.sh` не создает PostgreSQL-сервер и не настраивает systemd. Он подготавливает окружение проекта.

## 🧩 Ручная установка (если нужно)

Этот скрипт делает следующее:

1. Создает и активирует виртуальное окружение для `backend`
2. Устанавливает Python-зависимости из `backend/requirements.txt`
3. Копирует `backend/.env.example` в `backend/.env`, если файл отсутствует
4. Устанавливает Node.js зависимости в `frontend`
5. Создает `frontend/.env`, если файл отсутствует
6. Создает и активирует виртуальное окружение для `bot`
7. Устанавливает Python-зависимости из `bot/requirements.txt`
8. Копирует `bot/.env.example` в `bot/.env`, если файл отсутствует

### 3. Исправление кодировки

Если при запуске `init.bat` вы видите кракозябры, откройте командную строку в Windows Terminal и запустите:

```powershell
chcp 65001 >nul
init.bat
```

Скрипт уже содержит команду `chcp 65001 >nul`, поэтому при нормальном запуске он автоматически переключается на UTF-8.

Если проблема остается:

- Убедитесь, что файл `init.bat` сохранен в кодировке UTF-8
- Запустите скрипт через `cmd.exe`, а не через PowerShell встроенно
- Перезапустите терминал после установки Node.js

## 🧩 Ручная установка (если нужно)

### Backend

```powershell
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

### Frontend

```powershell
cd frontend
npm install
copy .env.example .env
```

### Bot

```powershell
cd bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

## 🚀 Запуск

### Backend

```powershell
cd backend
venv\Scripts\activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```powershell
cd frontend
npm run dev
```

### Bot

```powershell
cd bot
venv\Scripts\activate
python app.py
```

## 📝 Переменные окружения

### backend/.env

```env
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/smplat
SECRET_KEY=your-secret-key
DEBUG=True
```

### frontend/.env

```env
VITE_API_URL=http://localhost:8000/api
```

### bot/.env

```env
TOKEN=your_telegram_bot_token
BACKEND_API_URL=http://localhost:8000/api
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/smplat_bot
```

## 🛠️ Устранение неполадок

### npm не найден

```powershell
npm --version
```

Если команда не найдена, установите Node.js и перезапустите терминал.

### кодировка по-прежнему неправильная

- Откройте `init.bat` в VS Code
- Сохраните файл как UTF-8
- Запустите `cmd.exe` или Windows Terminal
- Выполните `chcp 65001 >nul`
- Запустите `init.bat`

## 🧱 Запуск как systemd сервисы (Ubuntu 22.04)

Для рабочего сервера удобно запускать `backend` и `bot` как системные службы.

### 1. Подготовка

Убедитесь, что проект развернут и все зависимости установлены через `./init.sh`.

Отредактируйте файлы:

- `backend/.env`
- `bot/.env`

### 2. Пример unit-файлов

- `deploy/backend.service`
- `deploy/bot.service`

Скопируйте их в `/etc/systemd/system/` и включите:

```bash
sudo cp deploy/backend.service /etc/systemd/system/smplat-backend.service
sudo cp deploy/bot.service /etc/systemd/system/smplat-bot.service
sudo systemctl daemon-reload
sudo systemctl enable --now smplat-backend.service
sudo systemctl enable --now smplat-bot.service
```

### 3. Проверка

```bash
sudo systemctl status smplat-backend.service
sudo systemctl status smplat-bot.service
sudo journalctl -u smplat-backend.service -f
sudo journalctl -u smplat-bot.service -f
```

### 4. Остановка / перезапуск

```bash
sudo systemctl stop smplat-backend.service
sudo systemctl start smplat-backend.service
sudo systemctl restart smplat-bot.service
```

> В unit-файлах пути к Python-окружению и рабочей директории нужно заменить на актуальные для вашего пользователя и сервера.
