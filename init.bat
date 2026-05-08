@echo off
REM Скрипт для инициализации проекта smplat на Windows

setlocal enabledelayedexpansion
cd /d "%~dp0"
chcp 65001 >nul

if errorlevel 1 (
    echo Ошибка: не удалось установить UTF-8 кодировку. Запустите этот скрипт в Windows Terminal или CMD с поддержкой UTF-8.
    pause
    exit /b 1
)

echo.
echo 🚀 Инициализация проекта Софтмонтаж...
echo.

REM 1. Backend
echo [1/4] Настройка Backend...
cd backend

if not exist "venv" (
    python -m venv venv
)

call venv\Scripts\activate.bat
pip install -q -r requirements.txt

if not exist ".env" (
    copy .env.example .env
    echo ✓ Создан backend\.env (отредактируйте с вашими данными БД)
) else (
    echo ✓ Backend .env уже существует
)

call venv\Scripts\deactivate.bat
cd ..

REM 2. Frontend
echo [2/4] Настройка Frontend...
cd frontend

if not exist "node_modules" (
    where npm >nul 2>&1
    if errorlevel 1 (
        echo Ошибка: npm не найден. Установите Node.js и повторите.
        exit /b 1
    )
    call npm install
    echo ✓ Frontend зависимости установлены
) else (
    echo ✓ Frontend зависимости уже установлены
)

if not exist ".env" (
    copy .env.example .env
    echo ✓ Создан frontend\.env
) else (
    echo ✓ Frontend .env уже существует
)

cd ..

REM 3. Bot
echo [3/4] Настройка Bot...
cd bot

if not exist "venv" (
    python -m venv venv
)

call venv\Scripts\activate.bat
pip install -q -r requirements.txt

if not exist ".env" (
    copy .env.example .env
    echo ✓ Создан bot\.env (добавьте TELEGRAM_BOT_TOKEN)
) else (
    echo ✓ Bot .env уже существует
)

call venv\Scripts\deactivate.bat
cd ..

REM 4. Summary
echo.
echo [4/4] Резюме...
echo.
echo ✓ Проект Софтмонтаж успешно инициализирован!
echo.
echo 📚 Дальнейшие действия:
echo.
echo 1️⃣  Backend:
echo    cd backend
echo    venv\Scripts\activate
echo    REM Отредактируйте .env с конфигурацией БД
echo    uvicorn app.main:app --reload
echo.
echo 2️⃣  Frontend (в новом терминале):
echo    cd frontend
echo    npm run dev
echo.
echo 3️⃣  Bot (в новом терминале):
echo    cd bot
echo    venv\Scripts\activate
echo    REM Отредактируйте .env с TELEGRAM_BOT_TOKEN
echo    python app.py
echo.

pause
