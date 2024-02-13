import time

from playwright.sync_api import sync_playwright


def test_lab01():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/iframe", wait_until="networkidle")
    page.frame_locator("#mce_0_ifr").locator("#tinymce").clear()
    page.frame_locator("#mce_0_ifr").locator("#tinymce").type("Hello Pramod")

    page.pause()

