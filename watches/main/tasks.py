import os

from telegram import Bot
from dotenv import load_dotenv
from celery import shared_task

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHANAL_ID = os.getenv('CHANAL_ID')

bot = Bot(token=TELEGRAM_TOKEN)


@shared_task
def send_message(
        name_form_view=None, datetime=None, request_number=None
):
    bot.send_message(
        chat_id=CHANAL_ID,
        text=(
            f'{name_form_view}: запрос под номером {request_number} '
            f'от {datetime}.'
        )
    )
