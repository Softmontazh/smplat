# Инструкция по запуску проекта Софтмонтаж

## � Лицензия

Этот проект является коммерческим программным обеспечением ТОО "Софтмонтаж". Подробности см. в [LICENSE.md](./LICENSE.md).

## �📋 Требования

- **Python 3.10+**
- **Node.js 18+**
- **PostgreSQL 13+**
- **Git**

## 🚀 Инициализация

### На Windows:
```bash
init.bat
```

### На Linux/Mac:
```bash
chmod +x init.sh
./init.sh
```

## 🔄 После инициализации

### 1️⃣ Запустите Backend (первая очередь!)

```bash
cd backend

# Активируйте виртуальное окружение
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Отредактируйте .env с вашей БД
# DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/smplat

# Запустите сервер
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

✅ Backend доступен: http://localhost:8000

### 2️⃣ Запустите Frontend (в новом терминале)

```bash
cd frontend
npm run dev
```

✅ Frontend доступен: http://localhost:3000

### 3️⃣ Запустите Bot (в новом терминале, опционально)

```bash
cd bot

# Активируйте виртуальное окружение
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows

# Отредактируйте .env с TELEGRAM_BOT_TOKEN
# TOKEN=ваш_токен_от_BotFather

# Запустите бота
python app.py
```

## 📚 API Documentation

После запуска Backend откройте в браузере:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🗄️ Инициализация БД

Backend создаст таблицы автоматически при первом запуске.

Если нужно пересоздать БД:

```bash
cd backend

# Удалить все таблицы
python -c "from app.db.engine import drop_tables; import asyncio; asyncio.run(drop_tables())"

# Создать таблицы заново
python -c "from app.db.engine import create_tables; import asyncio; asyncio.run(create_tables())"
```

## 🔍 Проверка

Убедитесь, что все компоненты работают:

```bash
# Backend health check
curl http://localhost:8000/health

# Frontend доступен
curl http://localhost:3000

# Bot запущен (если включен)
# Проверьте логи в терминале бота
```

## 🛠️ Команды разработки

### Backend
```bash
cd backend
# Форматирование кода
black app/

# Проверка типов
mypy app/

# Тесты
pytest
```

### Frontend
```bash
cd frontend
# Проверка типов
npm run type-check

# Lint
npm run lint

# Build
npm run build

# Preview production build
npm run preview
```

## 📝 Структура переменных окружения

### backend/.env
```
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/smplat
SECRET_KEY=your-secret-key-change-in-production
DEBUG=True
TELEGRAM_BOT_TOKEN=optional_token
```

### frontend/.env
```
VITE_API_URL=http://localhost:8000/api
```

### bot/.env
```
TOKEN=your_telegram_bot_token
BACKEND_API_URL=http://localhost:8000/api
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/smplat_bot
```

## ⚠️ Troubleshooting

### БД не подключается
- Проверьте, что PostgreSQL запущена
- Проверьте `DATABASE_URL` в `.env`
- Убедитесь, что БД создана: `createdb smplat`

### Port already in use
```bash
# Linux/Mac: найдите процесс на порту 8000
lsof -i :8000
kill -9 <PID>

# Windows: найдите процесс на порту 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Node modules проблемы
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
```

### Python dependencies проблемы
```bash
cd backend
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 📞 Поддержка

Если у вас возникли проблемы, обратитесь в:
- 📧 info@softmontazh.kz
- 🌐 https://softmontazh.kz
