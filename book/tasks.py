import time

import requests
from config.settings import TELEGRAM_BOT_TOKEN, CHAT_ID
from celery import shared_task


@shared_task
def send_telegram_notification(order_id, book_title, quantity, customer_username, phone_number):
    time.sleep(5)
    token = TELEGRAM_BOT_TOKEN
    method = 'sendMessage'

    message_text = f'🔔Yangi Buyurtma: {order_id}\n\n📚Kitob Nomi: {book_title}\n📌Soni: {quantity}\n' \
                   f'👤Mijoz: {customer_username}\n📞Tel: {phone_number}'

    respone = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': {CHAT_ID}, 'text': message_text}
    ).json()
