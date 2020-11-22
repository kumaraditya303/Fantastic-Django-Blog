# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from playwright.page import Page

from accounts.models import Author


def test_register(page: Page, live_server):
    page.goto(f"{live_server.url}/accounts/login/")
    page.click('text="Register"')
    assert page.url == f"{live_server.url}/accounts/register/"
    page.fill('input[name="username"]', "blah")
    page.fill('input[name="first_name"]', "blah")
    page.fill('input[name="last_name"]', "blah")
    page.fill('input[name="email"]', "blah@blah.com")
    page.fill('input[name="password1"]', "loremipsum123")
    page.fill('input[name="password2"]', "loremipsum123")
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/accounts/login/"
    assert User.objects.count() == 1
    assert Author.objects.count() == 1
    author = Author.objects.get(user__username="blah")
    assert author.user.username == "blah"
    assert author.user.email == "blah@blah.com"
    assert author.user.is_active
    assert not author.user.is_staff
    assert not author.user.is_superuser
    assert author.__str__() == author.user.get_full_name()


def test_login(page: Page, live_server):
    page.goto(f"{live_server.url}/accounts/login/")
    page.click('text="Register"')
    assert page.url == f"{live_server.url}/accounts/register/"
    page.fill('input[name="username"]', "blah")
    page.fill('input[name="first_name"]', "blah")
    page.fill('input[name="last_name"]', "blah")
    page.fill('input[name="email"]', "blah@blah.com")
    page.fill('input[name="password1"]', "loremipsum123")
    page.fill('input[name="password2"]', "loremipsum123")
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/accounts/login/"
    page.fill('input[name="username"]', "blah")
    page.fill('input[name="password"]', "loremipsum123")
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/"


def test_logout(page: Page, live_server) -> None:
    page.goto(f"{live_server.url}/accounts/login/")
    page.click('text="Register"')
    assert page.url == f"{live_server.url}/accounts/register/"
    page.fill('input[name="username"]', "blah")
    page.fill('input[name="first_name"]', "blah")
    page.fill('input[name="last_name"]', "blah")
    page.fill('input[name="email"]', "blah@blah.com")
    page.fill('input[name="password1"]', "loremipsum123")
    page.fill('input[name="password2"]', "loremipsum123")
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/accounts/login/"
    page.fill('input[name="username"]', "blah")
    page.fill('input[name="password"]', "loremipsum123")
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/"
    page.click('text="Logout"')
    assert page.url == f"{live_server.url}/accounts/logout/"


def test_account_update(page: Page, live_server):
    page.goto(f"{live_server.url}/accounts/login/")
    page.click('text="Register"')
    assert page.url == f"{live_server.url}/accounts/register/"
    page.fill('input[name="username"]', "blah")
    page.fill('input[name="first_name"]', "blah")
    page.fill('input[name="last_name"]', "blah")
    page.fill('input[name="email"]', "blah@blah.com")
    page.fill('input[name="password1"]', "loremipsum123")
    page.fill('input[name="password2"]', "loremipsum123")
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/accounts/login/"
    page.fill('input[name="username"]', "blah")
    page.fill('input[name="password"]', "loremipsum123")
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/"
    page.click('text="Profile"')
    assert page.url == f"{live_server.url}/accounts/profile/"
    page.fill('input[name="first_name"]', "test1")
    page.fill('input[name="last_name"]', "user1")
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/accounts/profile/"
