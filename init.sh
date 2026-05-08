#!/bin/bash
# Скрипт для инициализации проекта smplat

set -e

echo "🚀 Инициализация проекта Софтмонтаж..."
echo ""

# Detect Python interpreter
if command -v python3 >/dev/null 2>&1; then
    PYTHON=python3
elif command -v python >/dev/null 2>&1; then
    PYTHON=python
else
    echo "Ошибка: Python не найден. Установите python3."
    exit 1
fi

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 1. Backend
echo -e "${YELLOW}[1/4]${NC} Настройка Backend..."
cd backend
$PYTHON -m venv venv || echo "venv already exists"

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

$PYTHON -m pip install -q -r requirements.txt
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${GREEN}✓${NC} Created backend/.env (пожалуйста, отредактируйте с вашими данными БД)"
else
    echo -e "${GREEN}✓${NC} Backend .env уже существует"
fi
deactivate
cd ..

# 2. Frontend
echo -e "${YELLOW}[2/4]${NC} Настройка Frontend..."
cd frontend
if [ ! -d "node_modules" ]; then
    if ! command -v npm >/dev/null 2>&1; then
        echo "Ошибка: npm не найден. Установите Node.js и npm."
        exit 1
    fi
    npm install -q
    echo -e "${GREEN}✓${NC} Frontend зависимости установлены"
else
    echo -e "${GREEN}✓${NC} Frontend зависимости уже установлены"
fi

if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${GREEN}✓${NC} Created frontend/.env"
else
    echo -e "${GREEN}✓${NC} Frontend .env уже существует"
fi
cd ..

# 3. Bot
echo -e "${YELLOW}[3/4]${NC} Настройка Bot..."
cd bot
$PYTHON -m venv venv || echo "venv already exists"

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    source venv/Scripts/activate
else
    source venv/bin/activate
fi

$PYTHON -m pip install -q -r requirements.txt
if [ ! -f .env ]; then
    cp .env.example .env
    echo -e "${GREEN}✓${NC} Created bot/.env (пожалуйста, добавьте TELEGRAM_BOT_TOKEN)"
else
    echo -e "${GREEN}✓${NC} Bot .env уже существует"
fi
deactivate
cd ..

# 4. Summary
echo ""
echo -e "${YELLOW}[4/4]${NC} Резюме..."
echo ""
echo -e "${GREEN}✓ Проект Софтмонтаж успешно инициализирован!${NC}"
echo ""
echo "📚 Дальнейшие действия:"
echo ""
echo "1️⃣  Backend:"
echo "   cd backend"
echo "   source venv/bin/activate  # На Windows: venv\\Scripts\\activate"
echo "   # Отредактируйте .env с конфигурацией БД"
echo "   uvicorn app.main:app --reload"
echo ""
echo "2️⃣  Frontend (в новом терминале):"
echo "   cd frontend"
echo "   npm run dev"
echo ""
echo "3️⃣  Bot (в новом терминале):"
echo "   cd bot"
echo "   source venv/bin/activate"
echo "   # Отредактируйте .env с TELEGRAM_BOT_TOKEN"
echo "   python app.py"
echo ""
echo "📖 Документация: https://github.com/Softmontazh/smplat"
echo ""
