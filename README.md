# telegram-export

Экспорт чатов, каналов и личных переписок из Telegram через MTProto API.

## Установка

```bash
git clone https://github.com/shorin-nikita/telegram-export.git
cd telegram-export
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Настройка

Получите `API_ID` и `API_HASH` на [my.telegram.org/apps](https://my.telegram.org/apps), затем запустите:

```bash
tg-export setup
```

## Использование

```bash
# Публичный канал или пользователь
tg-export export https://t.me/durov --format json

# Приватная группа по ID
tg-export export https://t.me/c/1234567890

# За последние 7 дней с медиа
tg-export export @username --days 7 --media
```

Экспорт сохраняется в папку `exports/`.

## Лицензия

MIT
