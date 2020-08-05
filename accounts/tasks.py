from celery import shared_task
from django.core.mail import send_mail
from blog.models import Newsletter, Post

from django.template.loader import render_to_string


@shared_task
def send_newsletter():
    emails = list(Newsletter.objects.values_list('email', flat=True).all())
    latest_post = Post.objects.filter(
        featured=True).order_by('-timestamp').first()
    posts = Post.objects.order_by('-timestamp')[0:3]
    html = render_to_string('blog/newsletter.html',
                            context={"latest_post": latest_post,
                                     'posts': posts})
    print(emails)
    print(Post.objects.all())
    return send_mail("Your daily Newsletter", message="Newsletter",
                     recipient_list=emails,
                     from_email='admin@test.com',
                     html_message=html)
