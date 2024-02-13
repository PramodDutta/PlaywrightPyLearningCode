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
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    # Make page loaded
    page.wait_for_load_state("networkidle")
    page.get_by_role("checkbox").first.click()
    page.get_by_role("checkbox").last.uncheck()







    time.sleep(5)
