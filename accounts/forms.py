from accounts.models import Author
from django.contrib.auth.models import User
from django import forms

from django.contrib.auth.forms import UserCreationForm


class AuthorForm(forms.ModelForm):
    picture = forms.ImageField(required=False)

    class Meta:
        model = Author
        fields = ('picture',)


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
