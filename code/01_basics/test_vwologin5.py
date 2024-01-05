from playwright.sync_api import expect, sync_playwright


# Page - class -> Help you interact with HTML
# expect - Validate the message Exepected Resule == Actual Result
# Validation -> pytest - assert also avaiable.

def test_vwo_login():
    # 1. Browser and Page
    browser = sync_playwright().start().chromium.launch(headless=False)
    # create a new incognito browser context
    context = browser.new_context()

    page = context.new_page()


    # 2. Code Interaction with the HTML Web page
    page.goto("https://app.vwo.com")



    # 3. Validation
    expect(page).to_have_title("Login - VWO")

    # dispose context once it is no longer needed.
    context.close()
