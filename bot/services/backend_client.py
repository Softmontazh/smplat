# -*- coding: utf-8 -*-
"""
HTTP клиент для интеграции с backend API
"""

import httpx
import os
from typing import Optional, Dict, Any
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BACKEND_API_URL = os.getenv("BACKEND_API_URL", "http://localhost:8000/api")
BACKEND_API_TIMEOUT = int(os.getenv("BACKEND_API_TIMEOUT", "30"))


class BackendAPIClient:
    """Клиент для обращения к backend API"""

    def __init__(self):
        self.base_url = BACKEND_API_URL
        self.timeout = BACKEND_API_TIMEOUT

    async def create_task(self, task_data: Dict[str, Any]) -> Optional[Dict]:
        """Создать новую задачу в backend"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/tasks", json=task_data, timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Ошибка при создании задачи: {e}")
            return None

    async def get_task(self, task_id: int) -> Optional[Dict]:
        """Получить информацию о задаче"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/tasks/{task_id}", timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Ошибка при получении задачи: {e}")
            return None

    async def get_user(self, telegram_id: int) -> Optional[Dict]:
        """Получить пользователя по Telegram ID"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{self.base_url}/users/telegram/{telegram_id}",
                    timeout=self.timeout,
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Ошибка при получении пользователя: {e}")
            return None

    async def create_or_update_user(self, user_data: Dict[str, Any]) -> Optional[Dict]:
        """Создать или обновить пользователя"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/users", json=user_data, timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Ошибка при создании/обновлении пользователя: {e}")
            return None

    async def create_quote(self, quote_data: Dict[str, Any]) -> Optional[Dict]:
        """Создать смету/предложение"""
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/quotes", json=quote_data, timeout=self.timeout
                )
                response.raise_for_status()
                return response.json()
        except Exception as e:
            print(f"Ошибка при создании сметы: {e}")
            return None


# Глобальный экземпляр клиента
backend_client = BackendAPIClient()
