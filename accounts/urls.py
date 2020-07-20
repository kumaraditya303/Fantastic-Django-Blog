from django.urls import path
from accounts import views

urlpatterns = [
    path("author/<int:author>", views.author, name="author-detail"),
    path("register/", views.register, name="register"),
]
