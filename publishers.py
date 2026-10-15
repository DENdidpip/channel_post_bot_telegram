
import threading
import requests

from bot_instance import bot
from config import (
    CATS_CHANNEL_ID,
    DOGS_CHANNEL_ID,
    URL_FACTS_CATS,
    URL_PHOTOS_CATS,
    URL_FACTS_DOGS,
    URL_PHOTOS_DOGS,
    TIMESLEEP,
)

cat_stop = None
dog_stop = None

cat_thread = None
dog_thread = None

lock = threading.Lock()


def send_cat_facts(stop_event):
    while not stop_event.is_set():
        try:
            photo_response = requests.get(
                URL_PHOTOS_CATS, timeout=15
            )
            photo_response.raise_for_status()
            photo_data = photo_response.json()

            fact_response = requests.get(
                URL_FACTS_CATS, timeout=15
            )
            fact_response.raise_for_status()
            fact = fact_response.json()["fact"]

            # Не отправляем пост, если поток уже остановили
            if stop_event.is_set():
                break

            bot.send_photo(
                chat_id=CATS_CHANNEL_ID,
                photo=photo_data["url"],
                caption=fact,
            )

        except Exception as e:
            print("Cat error:", e)

        if stop_event.wait(TIMESLEEP):
            break


def send_dog_facts(stop_event):
    while not stop_event.is_set():
        try:
            fact_response = requests.get(
                URL_FACTS_DOGS, timeout=15
            )
            fact_response.raise_for_status()
            facts = fact_response.json().get(
                "facts", ["No fact found"]
            )

            photo_response = requests.get(
                URL_PHOTOS_DOGS, timeout=15
            )
            photo_response.raise_for_status()
            photo_data = photo_response.json()

            if stop_event.is_set():
                break

            bot.send_photo(
                chat_id=DOGS_CHANNEL_ID,
                photo=photo_data[0]["url"],
                caption=facts[0],
            )

        except Exception as e:
            print("Dog error:", e)

        if stop_event.wait(TIMESLEEP):
            break
