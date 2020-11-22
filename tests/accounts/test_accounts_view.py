# -*- coding: utf-8 -*-
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright import sync_playwright


class AccountsViewTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    def setUp(self) -> None:
        super().setUp()
        self.page = self.browser.newPage()

    def tearDown(self) -> None:
        self.page.close()
        super().tearDown()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.close()
        cls.playwright.stop()
        super().tearDownClass()

    def test_register(self) -> None:
        self.page.goto(f"{self.live_server_url}/accounts/login/")
        self.page.click('text="Register"')
        assert self.page.url == f"{self.live_server_url}/accounts/register/"
        self.page.fill('input[name="username"]', "blah")
        self.page.fill('input[name="first_name"]', "blah")
        self.page.fill('input[name="last_name"]', "blah")
        self.page.fill('input[name="email"]', "blah@blah.com")
        self.page.fill('input[name="password1"]', "loremipsum123")
        self.page.fill('input[name="password2"]', "loremipsum123")
        self.page.click('input[type="submit"]')
        assert self.page.url == f"{self.live_server_url}/accounts/login/"

    def test_login(self) -> None:
        self.page.goto(f"{self.live_server_url}/accounts/login/")
        self.page.click('text="Register"')
        assert self.page.url == f"{self.live_server_url}/accounts/register/"
        self.page.fill('input[name="username"]', "blah")
        self.page.fill('input[name="first_name"]', "blah")
        self.page.fill('input[name="last_name"]', "blah")
        self.page.fill('input[name="email"]', "blah@blah.com")
        self.page.fill('input[name="password1"]', "loremipsum123")
        self.page.fill('input[name="password2"]', "loremipsum123")
        self.page.click('input[type="submit"]')
        assert self.page.url == f"{self.live_server_url}/accounts/login/"
        self.page.fill('input[name="username"]', "blah")
        self.page.fill('input[name="password"]', "loremipsum123")
        self.page.click('input[type="submit"]')
        assert self.page.url == f"{self.live_server_url}/"

    def test_logout(self) -> None:
        self.page.goto(f"{self.live_server_url}/accounts/login/")
        self.page.click('text="Register"')
        assert self.page.url == f"{self.live_server_url}/accounts/register/"
        self.page.fill('input[name="username"]', "blah")
        self.page.fill('input[name="first_name"]', "blah")
        self.page.fill('input[name="last_name"]', "blah")
        self.page.fill('input[name="email"]', "blah@blah.com")
        self.page.fill('input[name="password1"]', "loremipsum123")
        self.page.fill('input[name="password2"]', "loremipsum123")
        self.page.click('input[type="submit"]')
        assert self.page.url == f"{self.live_server_url}/accounts/login/"
        self.page.fill('input[name="username"]', "blah")
        self.page.fill('input[name="password"]', "loremipsum123")
        self.page.click('input[type="submit"]')
        assert self.page.url == f"{self.live_server_url}/"
        self.page.click('text="Logout"')
        assert self.page.url == f"{self.live_server_url}/accounts/logout/"

    def test_account_update(self) -> None:
        self.page.goto(f"{self.live_server_url}/accounts/login/")
        self.page.click('text="Register"')
        assert self.page.url == f"{self.live_server_url}/accounts/register/"
        self.page.fill('input[name="username"]', "blah")
        self.page.fill('input[name="first_name"]', "blah")
        self.page.fill('input[name="last_name"]', "blah")
        self.page.fill('input[name="email"]', "blah@blah.com")
        self.page.fill('input[name="password1"]', "loremipsum123")
        self.page.fill('input[name="password2"]', "loremipsum123")
        self.page.click('input[type="submit"]')
        assert self.page.url == f"{self.live_server_url}/accounts/login/"
        self.page.fill('input[name="username"]', "blah")
        self.page.fill('input[name="password"]', "loremipsum123")
        self.page.click('input[type="submit"]')
        assert self.page.url == f"{self.live_server_url}/"
        self.page.click('text="Profile"')
        assert self.page.url == f"{self.live_server_url}/accounts/profile/"
        self.page.fill('input[name="first_name"]', "test1")
        self.page.fill('input[name="last_name"]', "user1")
        self.page.click('input[type="submit"]')
        assert self.page.url == f"{self.live_server_url}/accounts/profile/"
