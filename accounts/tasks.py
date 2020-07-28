from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_email():
    send_mail('Test', "Testing purposes", 'messmgmtsystem@gmail.com',
              ['test@gmail.com'])
    return None
