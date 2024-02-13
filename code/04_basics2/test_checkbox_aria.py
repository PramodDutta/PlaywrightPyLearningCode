import time

import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.mark.test
def test_vwo_login_negative():
    # Boilerplate code to star the Playright!
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Load the Page
    page.goto("https://awesomeqa.com/practice.html")
    # Make page loaded
    page.wait_for_load_state("networkidle")
    page.locator("//input[@id='profession-0']").click()

    page.locator("#continents").select_option("Africa")
    page.locator("//select[@id='selenium_commands']").sele("Navigation Commands")







    time.sleep(5)
