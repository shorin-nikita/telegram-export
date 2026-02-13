"""Загрузка и валидация конфигурации из .env файла."""

import os
import sys
from dotenv import load_dotenv


def _find_env_file():
    """Ищет .env файл: сначала в текущей директории, потом рядом с пакетом."""
    candidates = [
        os.path.join(os.getcwd(), ".env"),
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"),
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None


def load_config():
    """Загрузить конфигурацию из .env файла."""
    env_path = _find_env_file()
    if env_path:
        load_dotenv(env_path)


load_config()

API_ID = os.getenv("TELEGRAM_API_ID", "")
API_HASH = os.getenv("TELEGRAM_API_HASH", "")
SESSION_NAME = os.getenv("SESSION_NAME", "tg_export_session")
EXPORT_DIR = os.getenv("EXPORT_DIR", "exports")


def validate():
    """Проверить наличие обязательных параметров конфигурации."""
    if not API_ID or not API_HASH:
        print("Ошибка: не заданы TELEGRAM_API_ID и TELEGRAM_API_HASH.")
        print()
        print("Варианты настройки:")
        print("  1. Запустите: tg-export setup")
        print("  2. Или создайте .env файл вручную (см. .env.example)")
        print()
        print("Получите API ключи на https://my.telegram.org/apps")
        sys.exit(1)

    try:
        int(API_ID)
    except ValueError:
        print(f"Ошибка: TELEGRAM_API_ID должен быть числом, получено: {API_ID!r}")
        sys.exit(1)


def get_api_id():
    """Вернуть API_ID как int."""
    return int(API_ID)
