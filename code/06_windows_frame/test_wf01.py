import time

from playwright.sync_api import sync_playwright


def test_lab01():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/windows", wait_until="networkidle")

    # Use expect_popup() to capture the new tab when performing the action that opens it.
    with page.expect_popup() as popup_infor:
        page.get_by_role("link", name="Click here").click()

    page1 = popup_infor.value
    print(page1.text_content("h3"))

    page.bring_to_front()
    page.pause()

