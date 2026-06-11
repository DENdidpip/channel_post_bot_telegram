# 🐱🐶 Telegram Cat & Dog Facts Bot

A simple Telegram bot that automatically posts random cat and dog facts with images to Telegram channels.

## Features

* 🐱 Random cat facts with cat photos
* 🐶 Random dog facts with dog photos
* 🔒 Simple password-protected admin panel
* ⏱ Automatic posting every hour
* ▶ Start/Stop posting directly from Telegram
* 🌍 Uses public APIs for facts and images

## Technologies

* Python 3
* pyTelegramBotAPI
* Requests
* Python Dotenv
* Threading

## APIs Used

### Cats

* Facts: https://catfact.ninja/
* Images: https://cataas.com/

### Dogs

* Facts: https://dog-api.kinduff.com/
* Images: https://thedogapi.com/

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/cat-dog-facts-bot.git
cd cat-dog-facts-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
YOUR_TELEGRAM_BOT_TOKEN=YOUR_BOT_TOKEN

CHANNEL_WITH_CATS=@your_cat_channel
CHANNEL_WITH_DOGS=@your_dog_channel

CHOOSE_THE_PASSWORD=your_password
```

## Usage

Run the bot:

```bash
python main.py
```

Send the admin password to the bot.

After successful authentication, an admin panel will appear with two buttons:

* 🐱 Enable/Disable cat facts
* 🐶 Enable/Disable dog facts

The bot will automatically post content to the configured channels every hour.

## Project Structure

```text
project/
│
├── main.py
├── .env
├── requirements.txt
└── README.md
```

## Requirements

```text
certifi==2025.1.31
chardet==3.0.4
charset-normalizer==3.4.1
dotenv==0.9.9
googletrans==4.0.0rc1
h11==0.9.0
h2==3.2.0
hpack==3.0.0
hstspreload==2025.1.1
httpcore==0.9.1
httpx==0.13.3
hyperframe==5.2.0
idna==2.10
pyTelegramBotAPI==4.26.0
python-dotenv==1.2.2
requests==2.32.3
rfc3986==1.5.0
sniffio==1.3.1
telebot==0.0.5
urllib3==2.3.0
```

## Notes

This project was created as a small educational Telegram bot project. Feel free to modify and improve it.

=======
For starting to use this project, you have to fill this fields:

'''
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

cats_channal_ip = 'CHANNEL_WITH_CATS'
dogs_channal_ip = 'CHANNEL_WITH_DOGS'

password_for_panel = 'CHOOSE_THE_PASSWORD'
'''

It's a telegram bot with admin panel.

In this case, two channels are connected to the bot, in which it sends interesting 
photos and facts about cats and dogs every hour (the information is 
obtained from API keys that are publicly available).
