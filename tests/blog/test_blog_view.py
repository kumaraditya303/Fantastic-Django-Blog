# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright import sync_playwright

from accounts.models import Author
from blog.models import Category


class BlogViewTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    def setUp(self) -> None:
        super().setUp()
        self.page = self.browser.newPage()
        user = User.objects.create_user(
            username="test", email="normal@user.com", password="foobar123"
        )
        self.author = Author.objects.create(user=user)
        Category.objects.create(title="Test")
        self.page.goto(f"{self.live_server_url}/accounts/login/")
        self.page.fill('input[name="username"]', "test")
        self.page.fill('input[name="password"]', "foobar123")
        self.page.click('input[type="submit"]')

    def tearDown(self) -> None:
        self.page.close()
        super().tearDown()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.playwright.stop()
        super().tearDownClass()

    def test_index(
        self,
    ) -> None:
        self.page.click("text=Create Post")
        assert self.page.url == f"{self.live_server_url}/posts/create/"
        self.page.fill('input[name="title"]', "testing")
        self.page.fill('textarea[name="overview"]', "testing lorem ipsum")
        self.page.click("div.tox-edit-area")
        self.page.keyboard.insertText("Hello World")
        self.page.check('input[name="featured"]')
        self.page.selectOption('select[name="category"]', "1")
        self.page.click('input[type="submit"]')
        assert self.page.url == f"{self.live_server_url}/post/testing/"
