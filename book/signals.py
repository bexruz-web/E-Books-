from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .tasks import send_telegram_notification


@receiver(post_save, sender=Order)
def notify_admin(sender, instance, created, **kwargs):
    if created:  # Check if a new record is created
        send_telegram_notification.delay(
            order_id=instance.id,
            book_title=instance.book.title,
            quantity=instance.quantity,
            customer_username=instance.customer.username,
            phone_number=instance.phone_number
        )