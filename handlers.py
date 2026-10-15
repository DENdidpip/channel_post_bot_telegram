
import threading
from telebot import types

from bot_instance import bot
from config import ACCESS
import publishers


@bot.message_handler(content_types=["text"])
def cats(message):
    if message.from_user.id not in ACCESS:
        bot.send_message(message.chat.id, "Access denied")
        return

    if message.text == "🐱":
        with publishers.lock:
            if publishers.cat_thread is not None and publishers.cat_thread.is_alive():
                publishers.cat_stop.set()
                status = "OFF"
            else:
                publishers.cat_stop = threading.Event()
                publishers.cat_thread = threading.Thread(
                    target=publishers.send_cat_facts,
                    args=(publishers.cat_stop,),
                    daemon=True,
                )
                publishers.cat_thread.start()
                status = "ON"

        bot.send_message(message.chat.id, f"Part 'Cat' is {status}")

    elif message.text == "🐶":
        with publishers.lock:
            if publishers.dog_thread is not None and publishers.dog_thread.is_alive():
                publishers.dog_stop.set()
                status = "OFF"
            else:
                publishers.dog_stop = threading.Event()
                publishers.dog_thread = threading.Thread(
                    target=publishers.send_dog_facts,
                    args=(publishers.dog_stop,),
                    daemon=True,
                )
                publishers.dog_thread.start()
                status = "ON"

        bot.send_message(message.chat.id, f"Part 'Dog' is {status}")

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row(
            types.KeyboardButton("🐱"),
            types.KeyboardButton("🐶"),
        )

        bot.send_message(
            message.chat.id,
            "Hello admin",
            reply_markup=markup,
        )
