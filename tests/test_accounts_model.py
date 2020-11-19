# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import Author


class AccountsModelTestCase(TestCase):
    def test_create_user(self):

        user = User.objects.create_user(
            username="test", email="normal@user.com", password="foobar"
        )
        self.assertEqual(user.username, "test")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        author = Author.objects.create(user=user)
        self.assertEqual(author.user, user)
        self.assertEqual(author.__str__(), user.get_full_name())
