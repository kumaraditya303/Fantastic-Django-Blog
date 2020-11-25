# -*- coding: utf-8 -*-

from playwright.page import Page

from blog.models import Comment, Newsletter


def test_create_post(page: Page, live_server):
    page.click("text=Create Post")
    assert page.url == f"{live_server.url}/posts/create/"
    page.fill('input[name="title"]', "testing")
    page.fill('textarea[name="overview"]', "testing lorem ipsum")
    page.click("div.tox-edit-area")
    page.keyboard.insertText("Hello World")
    page.check('input[name="featured"]')
    page.selectOption('select[name="category"]', {"label": "Test"})
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/post/testing/"


def test_update_post(page: Page, live_server):
    page.click("text=Create Post")
    assert page.url == f"{live_server.url}/posts/create/"
    page.fill('input[name="title"]', "testing")
    page.fill('textarea[name="overview"]', "testing lorem ipsum")
    page.click("div.tox-edit-area")
    page.keyboard.insertText("Hello World")
    page.check('input[name="featured"]')
    page.selectOption('select[name="category"]', {"label": "Test"})
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/post/testing/"
    page.click("text=Update")
    page.fill('input[name="title"]', "testing2")
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/post/testing2/"
    assert "testing2" in page.textContent("#post-title")


def test_delete_post(page: Page, live_server):
    page.click("text=Create Post")
    assert page.url == f"{live_server.url}/posts/create/"
    page.fill('input[name="title"]', "testing")
    page.fill('textarea[name="overview"]', "testing lorem ipsum")
    page.click("div.tox-edit-area")
    page.keyboard.insertText("Hello World")
    page.check('input[name="featured"]')
    page.selectOption('select[name="category"]', {"label": "Test"})
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/post/testing/"
    page.click("text=Delete")
    page.click("text=Confirm")
    assert page.url == f"{live_server.url}/"


def test_newsletter(page: Page):
    page.fill('input[name="email"]', "test@test.com")
    page.click('input[type="submit"]')
    assert "Successfully subscribed!" in page.textContent('[role="alert"]')
    assert Newsletter.objects.count() == 2
    newsletter = Newsletter.objects.filter(email="test@test.com").first()
    assert newsletter.email == "test@test.com"
    assert newsletter.__str__() == "test@test.com"


def test_post_list(page: Page, live_server):
    page.click("text=Create Post")
    assert page.url == f"{live_server.url}/posts/create/"
    page.fill('input[name="title"]', "testing")
    page.fill('textarea[name="overview"]', "testing lorem ipsum")
    page.click("div.tox-edit-area")
    page.keyboard.insertText("Hello World")
    page.check('input[name="featured"]')
    page.selectOption('select[name="category"]', {"label": "Test"})
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/post/testing/"
    page.goto(f"{live_server.url}/post")
    assert page.url == f"{live_server.url}/post/"


def test_search(page: Page, live_server):
    page.click("text=Create Post")
    assert page.url == f"{live_server.url}/posts/create/"
    page.fill('input[name="title"]', "testing")
    page.fill('textarea[name="overview"]', "testing lorem ipsum")
    page.click("div.tox-edit-area")
    page.keyboard.insertText("Hello World")
    page.check('input[name="featured"]')
    page.selectOption('select[name="category"]', {"label": "Test"})
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/post/testing/"
    page.goto(f"{live_server.url}/search/?q=testing")
    assert "Search results are ..." in page.textContent("#search-result")
    assert "testing" in page.textContent("#post-title")


def test_comment(page: Page, live_server):
    page.click("text=Create Post")
    assert page.url == f"{live_server.url}/posts/create/"
    page.fill('input[name="title"]', "testing")
    page.fill('textarea[name="overview"]', "testing lorem ipsum")
    page.click("div.tox-edit-area")
    page.keyboard.insertText("Hello World")
    page.check('input[name="featured"]')
    page.selectOption('select[name="category"]', {"label": "Test"})
    page.click('input[type="submit"]')
    assert page.url == f"{live_server.url}/post/testing/"
    page.fill('textarea[name="content"]', "Test Comment")
    page.click("text=Submit Comment")
    assert page.url == f"{live_server.url}/post/testing/"
    assert Comment.objects.count() == 1
    comment = Comment.objects.filter(content="Test Comment").first()
    assert comment.content == "Test Comment"
    assert comment.__str__() == "blah"
