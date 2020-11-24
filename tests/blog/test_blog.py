# -*- coding: utf-8 -*-

from playwright.page import Page


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
