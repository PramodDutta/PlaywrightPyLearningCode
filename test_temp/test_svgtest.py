import time

from playwright.sync_api import sync_playwright
import allure

@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "John Doe")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")
def test_vwo_login():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amcharts.com/svg-maps/?map=india")

    # Handling a list of SVG elements
    states_list = page.locator("xpath=//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    # Iterating over elements and performing an action
    for state in states_list.element_handles():
        aria_label = state.get_attribute("aria-label")
        print(aria_label)
        if aria_label.strip() == "Tripura":
            state.click()
            break

    # page.pause()
    page.close()

