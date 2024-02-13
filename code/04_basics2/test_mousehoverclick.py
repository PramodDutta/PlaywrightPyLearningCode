import time

import pytest
from playwright.sync_api import sync_playwright, expect


def test_keyboard_click():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/")
    page.locator("//a[normalize-space()='Broken Images']").dblclick()
    time.sleep(5)
