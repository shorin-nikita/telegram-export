# JSON-схема экспорта

## Структура файла

Корневой объект содержит метаданные и массив сообщений.

```json
{
  "entity_info": { ... },
  "total_messages": 1000,
  "messages": [ ... ]
}
```

### entity_info

Метаданные источника. В старых экспортах может называться `chat_info` или `channel_info` — команды `update` и `analyze` поддерживают все варианты.

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | int | ID сущности в Telegram |
| `name` | string | Имя (для пользователей) или заголовок (для каналов/групп) |
| `type` | string | `User`, `Chat`, `Channel` |
| `username` | string/null | Username (без @) |
| `export_date` | string | ISO 8601 дата экспорта |

Дополнительные поля для каналов (`channel_info`):

| Поле | Тип | Описание |
|------|-----|----------|
| `about` | string/null | Описание канала |
| `participants_count` | int/null | Количество подписчиков |
| `created_date` | string/null | Дата создания канала |

## Сообщение

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | int | ID сообщения |
| `date` | string/null | ISO 8601 дата отправки |
| `edit_date` | string/null | ISO 8601 дата редактирования |
| `text` | string | Текст сообщения (пустая строка если нет текста) |
| `message_type` | string | `text`, `MessageMediaPhoto`, `MessageMediaDocument` и т.д. |
| `media_file` | string/null | Имя файла медиа (если скачан) |
| `topic_id` | int/null | ID топика форума |
| `sender` | object/null | Отправитель |
| `reply_to` | object/null | Ответ на сообщение |
| `forward_from` | object/null | Пересланное сообщение |
| `reactions` | array | Реакции |
| `views` | int/null | Количество просмотров |
| `forwards` | int/null | Количество пересылок |
| `post_author` | string/null | Автор поста (для каналов с подписями) |

### sender

| Поле | Тип | Описание |
|------|-----|----------|
| `id` | int | ID пользователя |
| `first_name` | string/null | Имя |
| `last_name` | string/null | Фамилия |
| `username` | string/null | Username |
| `phone` | string/null | Номер телефона (если доступен) |

### reply_to

| Поле | Тип | Описание |
|------|-----|----------|
| `message_id` | int | ID сообщения, на которое ответ |
| `top_id` | int/null | ID корневого сообщения треда |
| `forum_topic` | bool/null | Является ли ответом в топике форума |

### forward_from

| Поле | Тип | Описание |
|------|-----|----------|
| `date` | string/null | Дата оригинального сообщения |
| `from_id` | int/null | ID отправителя оригинала |
| `from_name` | string/null | Имя отправителя оригинала |

### reactions (элемент массива)

| Поле | Тип | Описание |
|------|-----|----------|
| `emoticon` | string/null | Эмодзи реакции |
| `count` | int | Количество |
