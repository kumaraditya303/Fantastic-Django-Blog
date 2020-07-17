from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now=True, auto_now_add=False)
    author = models.ForeignKey(
        User, verbose_name="user", on_delete=models.CASCADE)

    def __str__(self):
        return f'Post <{self.title}> <{self.date_posted}> <{self.author}>'
