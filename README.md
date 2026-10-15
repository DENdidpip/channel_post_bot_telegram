# 🐱🐶 Telegram Cat & Dog Facts Bot

A Telegram bot that automatically posts random cat and dog facts with photos to your channels. The admin controls posting directly from a chat with the bot: one tap to start or stop each feed.

## Features

- 🐱 Random cat fact + random cat photo
- 🐶 Random dog fact + random dog photo (with breed info)
- ⏱ Automatic posting every hour (interval is configurable)
- 🎛 Admin panel with 🐱 / 🐶 buttons to start and stop each feed independently
- 🔒 Access restricted to a whitelist of Telegram user IDs
- 🧵 Each feed runs in its own thread and stops cleanly
- 🛡 External API errors never crash the bot: a failed attempt is logged and the loop continues

## How It Works

1. The admin sends any message to the bot, and the bot shows a keyboard with 🐱 and 🐶 buttons.
2. Pressing a button starts the feed for the matching channel; pressing it again stops it.
3. While a feed is on, the bot posts immediately, then repeats every `TIMESLEEP` seconds.
4. Users who are not in `ACCESS` receive `Access denied`.

> ⚠️ Feed state is stored in memory only. After a restart both feeds are off, so turn them on again with the buttons.

## APIs Used

| Purpose | Service |
|---|---|
| Cat facts | [catfact.ninja](https://catfact.ninja/) |
| Cat photos | [CATAAS](https://cataas.com/) |
| Dog facts | [Dog API (kinduff)](https://dog-api.kinduff.com/) |
| Dog photos | [The Dog API](https://thedogapi.com/) |

## Technologies

- Python 3.9+
- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI)
- [Requests](https://requests.readthedocs.io/)
- [python-dotenv](https://github.com/theskumar/python-dotenv)
- `threading` (standard library)

## Project Structure

```text
dendidpip-channel_post_bot_telegram/
├── cat.py            # entry point: starts polling
├── bot_instance.py   # bot instance creation
├── config.py         # settings and environment variables
├── handlers.py       # message handlers and admin panel
├── publishers.py     # cat and dog posting threads
├── requirements.txt  # dependencies
└── README.md
```

## Installation

### 1. Get a token and prepare channels

1. Create a bot with [@BotFather](https://t.me/BotFather) and copy its token.
2. Create two channels (or use existing ones): one for cats, one for dogs.
3. Add the bot as an **administrator** of each channel with permission to post messages.
4. Find your Telegram user ID, for example with [@userinfobot](https://t.me/userinfobot).

### 2. Clone the repository

```bash
git clone https://github.com/dendidpip/channel_post_bot_telegram.git
cd channel_post_bot_telegram
```

### 3. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

The bot only needs three packages:

```bash
pip install pyTelegramBotAPI requests python-dotenv
```

### 4. Create a `.env` file

In the project root:

```env
YOUR_TELEGRAM_BOT_TOKEN=123456:ABC-DEF...

CHANNEL_WITH_CATS=@your_cat_channel
CHANNEL_WITH_DOGS=@your_dog_channel

# Comma-separated Telegram IDs of admins
ACCESS=123456789,987654321
```

| Variable | Required | Description |
|---|---|---|
| `YOUR_TELEGRAM_BOT_TOKEN` | ✅ | Bot token from @BotFather |
| `CHANNEL_WITH_CATS` | ✅ | Cat channel: `@username` or numeric ID (`-100...`) |
| `CHANNEL_WITH_DOGS` | ✅ | Dog channel: `@username` or numeric ID |
| `ACCESS` | ✅ | Comma-separated admin Telegram IDs. If empty, nobody gets access |

If the token or either channel is missing, the bot exits with `Check your .env file!`.

> 🔐 Never commit `.env` to the repository. Add it to `.gitignore`.

## Usage

```bash
python cat.py
```

Open a chat with the bot and send any message. A keyboard will appear:

| Button | Action |
|---|---|
| 🐱 | Start / stop cat posts |
| 🐶 | Start / stop dog posts |

The bot replies with `Part 'Cat' is ON` or `Part 'Cat' is OFF` (same for dogs).

## Configuration

All settings live in `config.py`:

| Parameter | Default | Description |
|---|---|---|
| `TIMESLEEP` | `3600` | Interval between posts, in seconds |
| `URL_FACTS_CATS`, `URL_PHOTOS_CATS` | see file | Cat fact and photo sources |
| `URL_FACTS_DOGS`, `URL_PHOTOS_DOGS` | see file | Dog fact and photo sources |
