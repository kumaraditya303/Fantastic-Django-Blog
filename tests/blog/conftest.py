# -*- coding: utf-8 -*-
import pytest
from playwright.page import Page

from blog.models import Category


@pytest.fixture(autouse=True)
def create_test_data():
    Category.objects.create(title="Test")


@pytest.fixture
def page(page: Page, live_server):
    page.goto(f"{live_server.url}/accounts/login/")
    page.click('text="Register"')
    page.fill('input[name="username"]', "blah")
    page.fill('input[name="first_name"]', "blah")
    page.fill('input[name="last_name"]', "blah")
    page.fill('input[name="email"]', "blah@blah.com")
    page.fill('input[name="password1"]', "loremipsum123")
    page.fill('input[name="password2"]', "loremipsum123")
    page.click('input[type="submit"]')
    page.fill('input[name="username"]', "blah")
    page.fill('input[name="password"]', "loremipsum123")
    page.click('input[type="submit"]')
    yield page
