# telegram-export

Экспорт и анализ Telegram чатов, каналов и личных переписок.

Работает через Telegram MTProto API (Telethon) — без ботов, без ограничений Bot API.

## Быстрый старт

### 1. Установка

```bash
git clone https://github.com/your-username/telegram-export.git
cd telegram-export
pip install -e .
```

### 2. Настройка

```bash
tg-export setup
```

Скрипт попросит ввести `API_ID` и `API_HASH` (получите на [my.telegram.org/apps](https://my.telegram.org/apps)), создаст `.env` файл и авторизует вас в Telegram.

### 3. Экспорт

```bash
tg-export export https://t.me/durov --format json
```

Готово! Экспорт сохранен в папке `exports/`.

## Команды

### `tg-export setup`

Первоначальная настройка: создает `.env` файл с API ключами и авторизует в Telegram.

### `tg-export auth`

Повторная авторизация (если сессия истекла).

### `tg-export export <source>`

Универсальный экспорт сообщений из любого источника.

```bash
# Публичный канал или пользователь
tg-export export https://t.me/durov
tg-export export @username

# Приватная группа (по ID из URL)
tg-export export https://t.me/c/1234567890

# По номеру телефона
tg-export export "+79001234567"

# Формат: json (по умолчанию), txt, md
tg-export export @username --format md

# Только последние 7 дней
tg-export export @username --days 7

# С медиа-файлами (фото, видео, документы)
tg-export export @username --media

# Топик форума
tg-export export https://t.me/c/1234567890 --topic 123

# Всё вместе
tg-export export https://t.me/c/1234567890 --format md --days 30 --media
```

**Параметры:**

| Параметр | Описание |
|----------|----------|
| `--format`, `-f` | Формат: `json`, `txt`, `md` (по умолчанию `json`) |
| `--output`, `-o` | Свой путь для файла |
| `--topic`, `-t` | ID топика форума |
| `--media`, `-m` | Скачать медиа-файлы |
| `--days`, `-d` | Только за последние N дней |

### `tg-export update <path.json>`

Добавить новые сообщения в существующий JSON-экспорт.

```bash
tg-export update exports/Durov/export_20250101_120000.json
tg-export update exports/Durov/export_20250101_120000.json --no-media
```

### `tg-export download-media <path.json>`

Докачать медиа-файлы, которые указаны в экспорте, но отсутствуют на диске.

```bash
tg-export download-media exports/Chat/export.json
```

### `tg-export analyze <path.json>`

Офлайн-анализ экспорта. Генерирует отчет в `.md` и сырые данные в `.json`.

```bash
tg-export analyze exports/Group/export.json
tg-export analyze exports/Group/export.json --output report.md
```

Отчет включает:
- Общую статистику
- Топ участников
- Анализ топиков/тредов
- Временные паттерны (часы, дни недели, месяцы)
- Анализ контента (слова, ссылки, эмодзи)
- Вовлеченность (реакции, просмотры, пересылки)

### `tg-export channel-check <user>`

Проверить, владеет ли пользователь каналом.

```bash
tg-export channel-check @username
tg-export channel-check 123456789
```

### `tg-export channel-export <channel>`

Полный экспорт канала в JSON и TXT с информацией о подписчиках.

```bash
tg-export channel-export @channel_name
```

### `tg-export channel-stats <channel>`

Аналитический отчет по каналу: просмотры, реакции, пересылки, топ постов.

```bash
tg-export channel-stats @channel_name
```

## Форматы источников

| Формат | Пример | Описание |
|--------|--------|----------|
| URL приватного чата | `https://t.me/c/1234567890` | Группа или канал по ID |
| URL публичного | `https://t.me/username` | Канал, группа или пользователь |
| Username | `@username` | Любая сущность по username |
| Телефон | `+79001234567` | Пользователь по номеру |
| Числовой ID | `1234567890` | Пользователь или чат по ID |

## Структура экспорта

```
exports/
  ChatName/
    export_20250101_120000.json   # Сообщения
    export_20250101_120000.md     # Markdown версия
    media/                        # Медиа-файлы (если --media)
      20250101_120000_123.jpg
      20250101_120100_124.mp4
```

### JSON-формат

```json
{
  "entity_info": {
    "id": 123456789,
    "name": "Chat Name",
    "type": "Channel",
    "username": "channel_name",
    "export_date": "2025-01-01T12:00:00"
  },
  "total_messages": 1000,
  "messages": [
    {
      "id": 1,
      "date": "2025-01-01T12:00:00+00:00",
      "edit_date": null,
      "text": "Hello!",
      "message_type": "text",
      "media_file": null,
      "topic_id": null,
      "sender": {
        "id": 123,
        "first_name": "John",
        "last_name": "Doe",
        "username": "johndoe",
        "phone": null
      },
      "reply_to": null,
      "forward_from": null,
      "reactions": [],
      "views": null,
      "forwards": null,
      "post_author": null
    }
  ]
}
```

## Конфигурация

Конфигурация хранится в `.env` файле:

```env
TELEGRAM_API_ID=12345
TELEGRAM_API_HASH=abc123def456
SESSION_NAME=tg_export_session
EXPORT_DIR=exports
```

| Переменная | Обязательная | Описание |
|-----------|-------------|----------|
| `TELEGRAM_API_ID` | Да | ID приложения с my.telegram.org |
| `TELEGRAM_API_HASH` | Да | Hash приложения с my.telegram.org |
| `SESSION_NAME` | Нет | Имя файла сессии (по умолчанию `tg_export_session`) |
| `EXPORT_DIR` | Нет | Папка для экспортов (по умолчанию `exports`) |

## Альтернативный запуск

```bash
# Через python -m
python -m tg_export export @username

# Без установки (с requirements.txt)
pip install -r requirements.txt
python -m tg_export export @username
```

## Лицензия

MIT
