from django.contrib import admin

from blog.models import Category, Comment, Post, Newsletter

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Newsletter)
