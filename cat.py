import telebot
import requests
import time
import threading
from telebot import types

url_facts_cats = "https://catfact.ninja/fact"
url_photos_cats = "https://cataas.com/cat?json=true"
url_facts_dogs = "https://dog-api.kinduff.com/api/facts"
url_photos_dogs = "https://api.thedogapi.com/v1/images/search?size=med&mime_types=jpg&format=json&has_breeds=true&order=RANDOM&page=0&limit=1"

bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

cats_channal_ip = 'CHANNEL_WITH_CATS'
dogs_channal_ip = 'CHANNEL_WITH_DOGS'

password_for_panel = 'CHOOSE_THE_PASSWORD'

secure = False
catt = False
dogg = False

timesleep = 3600 #messages in channels every hour
def send_cat_facts():
    global catt
    while catt:
        try:
            response_c = requests.get(url_photos_cats)
            response1_c = requests.get(url_facts_cats)

            fact_data = response1_c.json()
            photo_data = response_c.json()

            bot.send_photo(chat_id=cats_channel_ip, photo=photo_data["url"], caption=fact_data["fact"])
        except Exception as e:
            bot.send_message(cats_channel_ip, f"Admin has no facts(: {str(e)}")
        time.sleep(timesleep)

def send_dog_facts():
    global dogg
    while dogg:
        try:
            response1_d = requests.get(url_facts_dogs)
            response_d = requests.get(url_photos_dogs)

            parsed_data = response1_d.json()
            facts = parsed_data.get('facts', ["No fact found"])

            photo_data_d = response_d.json()

            bot.send_photo(chat_id=dogs_channel_ip, photo=photo_data_d[0]["url"], caption=facts[0])

        except requests.exceptions.RequestException as e:
            bot.send_message(dogs_channel_ip, f"Error fetching dog facts: {str(e)}")

        time.sleep(timesleep)



@bot.message_handler(content_types=['text'])
def cats(message):
    global catt, dogg, secure

    if message.text == password_for_panel:
        secure = True
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🐱')
        btn2 = types.KeyboardButton('🐶')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, "Hello admin", reply_markup=markup)

    if secure:
        if message.text == '🐱':
            if not catt:
                catt = True
                bot.send_message(message.chat.id, "Part 'Cat' is ON")
                threading.Thread(target=send_cat_facts, daemon=True).start()
            else:
                catt = False
                bot.send_message(message.chat.id, "Part 'Cat' is OFF")

        elif message.text == '🐶':
            if not dogg:
                dogg = True
                bot.send_message(message.chat.id, "Part 'Dog' is ON")
                threading.Thread(target=send_dog_facts, daemon=True).start()
            else:
                dogg = False
                bot.send_message(message.chat.id, "Part 'Dog' is OFF")
    else:
        bot.send_message(message.chat.id, "Access denied")

bot.polling(none_stop=True)

