
import threading
from telebot import types

from bot_instance import bot
from config import ACCESS
import publishers


@bot.message_handler(content_types=["text"])
def cats(message):
    # Проверяем доступ
    if message.from_user.id not in ACCESS:
        bot.send_message(message.chat.id, "Access denied")
        print("Someone is trying to get access")
        return

    # Если нажали кнопку котов
    if message.text == "🐱":
        with publishers.lock:
            publishers.catt = not publishers.catt
            enabled = publishers.catt

        if enabled:
            threading.Thread(
                target=publishers.send_cat_facts,
                daemon=True
            ).start()

            bot.send_message(
                message.chat.id,
                "Part 'Cat' is ON"
            )
        else:
            bot.send_message(
                message.chat.id,
                "Part 'Cat' is OFF"
            )

    # Если нажали кнопку собак
    elif message.text == "🐶":
        with publishers.lock:
            publishers.dogg = not publishers.dogg
            enabled = publishers.dogg

        if enabled:
            threading.Thread(
                target=publishers.send_dog_facts,
                daemon=True
            ).start()

            bot.send_message(
                message.chat.id,
                "Part 'Dog' is ON"
            )
        else:
            bot.send_message(
                message.chat.id,
                "Part 'Dog' is OFF"
            )

    # Для любого другого текста показываем меню
    else:
        markup = types.ReplyKeyboardMarkup(
            resize_keyboard=True
        )

        markup.row(
            types.KeyboardButton("🐱"),
            types.KeyboardButton("🐶")
        )

        bot.send_message(
            message.chat.id,
            "Hello admin",
            reply_markup=markup
        )
