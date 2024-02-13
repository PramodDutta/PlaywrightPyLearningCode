import time

from playwright.sync_api import sync_playwright


def test_lab01():
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

    page.pause()

