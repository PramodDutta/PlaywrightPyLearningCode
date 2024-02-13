import time

from playwright.sync_api import sync_playwright


def test_lab01():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://awesomeqa.com/hr/web/index.php/auth/login")
    page.locator("[name='username']").fill("admin")
    page.locator("[name='password']").fill("Hacker@4321")
    page.click("//button[contains(@class, 'orangehrm-login-button')]")
    time.sleep(5)

