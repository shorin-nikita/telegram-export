# telegram-export

Export Telegram chats, channels and DMs via MTProto API.

## Install

```bash
git clone https://github.com/shorin-nikita/telegram-export.git
cd telegram-export
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

## Setup

Get `API_ID` and `API_HASH` at [my.telegram.org/apps](https://my.telegram.org/apps), then run:

```bash
tg-export setup
```

## Usage

```bash
# Public channel or user
tg-export export https://t.me/durov --format json

# Private group by ID
tg-export export https://t.me/c/1234567890

# Last 7 days with media
tg-export export @username --days 7 --media
```

Exports are saved to `exports/`.

## License

MIT
