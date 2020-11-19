# -*- coding: utf-8 -*-
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright import sync_playwright


class AccountsViewTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch()

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        super().tearDownClass()

    def test_register(self):
        page = self.browser.newPage()
        page.goto(f"{self.live_server_url}/accounts/login/")
        page.click('text="Login / SignUp"')
        page.goto(f"{self.live_server_url}/accounts/login/")
        page.click('text="Register"')
        assert page.url == f"{self.live_server_url}/accounts/register/"
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="first_name"]', "blah")
        page.fill('input[name="last_name"]', "blah")
        page.fill('input[name="email"]', "blah@blah.com")
        page.fill('input[name="password1"]', "loremipsum123")
        page.fill('input[name="password2"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == f"{self.live_server_url}/accounts/login/"
        page.close()

    def test_login(self):
        page = self.browser.newPage()
        page.goto(f"{self.live_server_url}/accounts/login/")
        page.click('text="Register"')
        assert page.url == f"{self.live_server_url}/accounts/register/"
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="first_name"]', "blah")
        page.fill('input[name="last_name"]', "blah")
        page.fill('input[name="email"]', "blah@blah.com")
        page.fill('input[name="password1"]', "loremipsum123")
        page.fill('input[name="password2"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == f"{self.live_server_url}/accounts/login/"
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="password"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == f"{self.live_server_url}/"
        page.close()

    def test_logout(self):
        page = self.browser.newPage()
        page.goto(f"{self.live_server_url}/accounts/login/")
        page.click('text="Register"')
        assert page.url == f"{self.live_server_url}/accounts/register/"
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="first_name"]', "blah")
        page.fill('input[name="last_name"]', "blah")
        page.fill('input[name="email"]', "blah@blah.com")
        page.fill('input[name="password1"]', "loremipsum123")
        page.fill('input[name="password2"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == f"{self.live_server_url}/accounts/login/"
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="password"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == f"{self.live_server_url}/"
        page.click('text="Logout"')
        assert page.url == f"{self.live_server_url}/accounts/logout/"
        page.close()

    def test_account_update(self):
        page = self.browser.newPage()
        page.goto(f"{self.live_server_url}/accounts/login/")
        page.click('text="Register"')
        assert page.url == f"{self.live_server_url}/accounts/register/"
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="first_name"]', "blah")
        page.fill('input[name="last_name"]', "blah")
        page.fill('input[name="email"]', "blah@blah.com")
        page.fill('input[name="password1"]', "loremipsum123")
        page.fill('input[name="password2"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == f"{self.live_server_url}/accounts/login/"
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="password"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == f"{self.live_server_url}/"
        page.click('text="Profile"')
        assert page.url == f"{self.live_server_url}/accounts/profile/"
        page.fill('input[name="first_name"]', "test1")
        page.fill('input[name="last_name"]', "user1")
        page.click('input[type="submit"]')
        assert page.url == f"{self.live_server_url}/accounts/profile/"
        page.close()
