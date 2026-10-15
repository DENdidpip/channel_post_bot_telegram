import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("YOUR_TELEGRAM_BOT_TOKEN")
CATS_CHANNEL_ID = os.getenv("CHANNEL_WITH_CATS")
DOGS_CHANNEL_ID = os.getenv("CHANNEL_WITH_DOGS")

ACCESS = [
    int(x.strip())
    for x in os.getenv("ACCESS", "").split(",")
    if x.strip()
]

if not all([TOKEN, CATS_CHANNEL_ID, DOGS_CHANNEL_ID]):
    raise ValueError("Check your .env file!")

URL_FACTS_CATS = "https://catfact.ninja/fact"
URL_PHOTOS_CATS = "https://cataas.com/cat?json=true"

URL_FACTS_DOGS = "https://dog-api.kinduff.com/api/facts"
URL_PHOTOS_DOGS = (
    "https://api.thedogapi.com/v1/images/search"
    "?size=med&mime_types=jpg&format=json&has_breeds=true&limit=1"
)

TIMESLEEP = 3600