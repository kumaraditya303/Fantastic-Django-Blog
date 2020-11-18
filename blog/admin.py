# -*- coding: utf-8 -*-
from django.contrib import admin

from blog.models import Category, Comment, Newsletter, Post

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Newsletter)
