# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.urls import path

from accounts import views

urlpatterns = [
    path(
        "accounts/register/", views.AuthorCreateView.as_view(), name="accounts_register"
    ),
    path(
        "accounts/profile/",
        login_required(views.AuthorUpdateView.as_view()),
        name="accounts_update",
    ),
]
