from django.contrib import admin

from blog.models import Author, Category, Comment, Post

# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
