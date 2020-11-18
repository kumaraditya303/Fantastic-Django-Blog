# -*- coding: utf-8 -*-
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from playwright import sync_playwright


class AccountTestCase(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.playwright = sync_playwright().start()
        cls.browser = cls.playwright.chromium.launch(headless=False)

    @classmethod
    def tearDownClass(cls):
        cls.browser.close()
        cls.playwright.stop()
        super().tearDownClass()

    def test_register(self):
        page = self.browser.newPage()
        page.goto("%s%s" % (self.live_server_url, "/accounts/login/"))
        page.click('text="Login / SignUp"')
        assert page.url == "%s%s" % (self.live_server_url, "/accounts/login/")
        page.click('text="Register"')
        assert page.url == "%s%s" % (self.live_server_url, "/accounts/register/")
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="first_name"]', "blah")
        page.fill('input[name="last_name"]', "blah")
        page.fill('input[name="email"]', "blah@blah.com")
        page.fill('input[name="password1"]', "loremipsum123")
        page.fill('input[name="password2"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == "%s%s" % (self.live_server_url, "/accounts/login/")
        page.close()

    def test_login(self):
        page = self.browser.newPage()
        page.goto("%s%s" % (self.live_server_url, "/accounts/login/"))
        page.click('text="Register"')
        assert page.url == "%s%s" % (self.live_server_url, "/accounts/register/")
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="first_name"]', "blah")
        page.fill('input[name="last_name"]', "blah")
        page.fill('input[name="email"]', "blah@blah.com")
        page.fill('input[name="password1"]', "loremipsum123")
        page.fill('input[name="password2"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == "%s%s" % (self.live_server_url, "/accounts/login/")
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="password"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == "%s%s" % (self.live_server_url, "/")
        page.close()

    def test_logout(self):
        page = self.browser.newPage()
        page.goto("%s%s" % (self.live_server_url, "/accounts/login/"))
        page.click('text="Register"')
        assert page.url == "%s%s" % (self.live_server_url, "/accounts/register/")
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="first_name"]', "blah")
        page.fill('input[name="last_name"]', "blah")
        page.fill('input[name="email"]', "blah@blah.com")
        page.fill('input[name="password1"]', "loremipsum123")
        page.fill('input[name="password2"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == "%s%s" % (self.live_server_url, "/accounts/login/")
        page.fill('input[name="username"]', "blah")
        page.fill('input[name="password"]', "loremipsum123")
        page.click('input[type="submit"]')
        assert page.url == "%s%s" % (self.live_server_url, "/")
        page.click('text="Logout"')
        assert page.url == "%s%s" % (self.live_server_url, "/accounts/logout/")
        page.close()
