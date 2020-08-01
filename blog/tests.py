from django.test import TestCase
from blog.models import Post
from django.contrib.auth.models import User
from accounts.models import Author


class PostTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="Test", password="testingpassword")
        Author.objects.create(user=user)

    def test_user_model(self):
        user = User.objects.first()
        author = Author.objects.first()
        self.assertIsInstance(user, User)
        self.assertIsInstance(author, Author)
