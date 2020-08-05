# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from accounts.models import Author


class AuthorForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = Author
        fields = ("picture",)


class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name")
