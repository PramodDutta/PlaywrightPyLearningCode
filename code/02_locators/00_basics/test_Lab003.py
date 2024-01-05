import time

from playwright.sync_api import expect, sync_playwright


# Page - class -> Help you interact with HTML
# expect - Validate the message Expected Result == Actual Result
# Validation -> pytest - assert also available.

def test_vwo_login():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Load the Page
    page.goto("https://awesomeqa.com/pw/locators1.html")
    # Make page loaded
    page.wait_for_load_state("networkidle")

    page.get_by_label("Subscribe").check()
    page.get_by_role("button",name="Submit").click()



    expect(page.get_by_role("listitem")).to_have_count(5)

    for row in page.get_by_role("listitem").all():
        print(row.text_content())


    time.sleep(10)




    # dispose context once it is no longer needed.
    context.close()
