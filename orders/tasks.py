from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Order


@shared_task
def send_order_confirmation_email(order_id, user_email):
    order = Order.objects.get(id=order_id)
    subject = "Order Confirmation"
    message = f"Thank you for your order {order.id}! Amount: {order.total_cost}"
    return send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])