from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_email():
    return send_mail('Test', "Testing purposes", 'messmgmtsystem@gmail.com',
              ['rahuladitya303@gmail.com'])
