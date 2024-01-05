import time

import pytest
from playwright.sync_api import sync_playwright, expect


@pytest.fixture()
def setUp():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page
    yield page
    page.close()
    context.close()


@pytest.mark.negative
def test_vwo_login_negative(setUp):
    page = setUp
    # Load the Page
    page.goto("https://katalon-demo-cura.herokuapp.com/")
    # Make page loaded
    page.wait_for_load_state("networkidle")

    expect(page).to_have_title("CURA Healthcare Service")
    page.locator("//a[@id='btn-make-appointment']").click()
    page.locator("#txt-username").fill("John Doe")
    page.locator("[name='password']").fill("ThisIsNotAPassword")
    page.locator("#btn-login").click()

    page.wait_for_load_state("networkidle")
    expect(page).to_have_url("https://katalon-demo-cura.herokuapp.com/#appointment")

    page.locator("//textarea[@id='txt_comment']").fill("I have fever 101")
    page.locator("//input[@id='txt_visit_date']").fill("05/01/2024")
    page.locator("//input[@id='txt_visit_date']").press('Enter')
    time.sleep(5)
    page.locator("#btn-book-appointment").click()

    result = page.locator("//h2[normalize-space()='Appointment Confirmation']").text_content()

    assert result == "Appointment Confirmation"

    time.sleep(5)
