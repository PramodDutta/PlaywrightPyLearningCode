import time

from playwright.sync_api import sync_playwright


def test_dowload_file():
    browser = sync_playwright().start().chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")

    with page.expect_download() as d:
        page.locator("//tbody/tr[1]/td[5]/a[1]").click()
    d = d.value
    file_path = d.path()
    print(f"File downloaded to: {file_path}")

    time.sleep(5)
