import os

from telegram import Bot
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHANAL_ID = os.getenv('CHANAL_ID')

bot = Bot(token=TELEGRAM_TOKEN)


def send_message():
    bot.send_message(
        chat_id=CHANAL_ID, text='Text_message'
    )
