import time

from playwright.sync_api import sync_playwright


def test_lab01():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://thetestingacademy.com/')
    title = page.evaluate("() => document.title")
    assert title == "TheTestingAcademy | Learn Software Testing and Automation Testing", "Title does not match"

    # Execute a more complex script
    script = """
            (message) => {
                return message;
            }
            """
    result = page.evaluate(script, "Hello, Playwright!")
    assert result == "Hello, Playwright!", "Script result does not match"


    page.pause()

