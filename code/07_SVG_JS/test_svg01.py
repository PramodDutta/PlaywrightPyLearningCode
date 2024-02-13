import time

from playwright.sync_api import sync_playwright


def test_lab01():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://flipkart.com")
    page.set_viewport_size({"width": 1200, "height": 800})
    #Interacting with the search input
    search_input = page.locator("input[name='q']")
    search_input.fill("AC")

    # Clicking on the SVG element
    search_element = page.locator("xpath=//button[@title='Search for Products, Brands and More']//*[name()='svg']")
    search_element.click()

    page.pause()

