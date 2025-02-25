import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from config.settings import TELEGRAM_BOT_TOKEN, CHAT_ID

from .models import Order


@receiver(post_save, sender=Order)
def notify_admin(sender, instance, created, **kwargs):
    if created:  # Check if a new record is created
        token = TELEGRAM_BOT_TOKEN
        method = 'sendMessage'

        # Prepare the message text (replace this with actual order details)
        message_text = f'Yangi Buyurtma: {instance.id}\n\nProduct: {instance.book.title}\nQuantity: {instance.quantity}\n' \
                       f'Client: {instance.customer.username}\nTel: {instance.phone_number}'

        respone = requests.post(
            url=f'https://api.telegram.org/bot{token}/{method}',
            data={'chat_id': {CHAT_ID}, 'text': message_text}
        ).json()
