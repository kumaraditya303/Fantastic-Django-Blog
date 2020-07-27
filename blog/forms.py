from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE

from blog.models import Author, Comment, Post


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={
        'cols': 80,
        'rows': 15,
        'class': 'form-control'
    }))

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content',
                  'featured', 'category', 'thumbnail')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("content",)
