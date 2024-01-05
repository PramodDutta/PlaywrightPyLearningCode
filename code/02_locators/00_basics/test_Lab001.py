from playwright.sync_api import expect, sync_playwright


# Page - class -> Help you interact with HTML
# expect - Validate the message Expected Result == Actual Result
# Validation -> pytest - assert also available.

def test_vwo_login():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Load the Page
    page.goto("https://app.vwo.com")
    # Make page loaded
    page.wait_for_load_state("networkidle")

    # Find the email and password
    # Email ID
    page.locator("#login-username").fill("admin")

    # Password
    page.locator("#login-password").fill("password123")

    # Click on the Submit
    page.locator("#js-login-btn").click()

    # Verify the message

    error_message = page.locator("#js-notification-box-msg")

    expect(error_message).to_have_text("Your email, password, IP address or location did not match")

    # dispose context once it is no longer needed.
    context.close()
