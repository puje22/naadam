from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    page.goto("https://www.devjee.mn/t", wait_until="networkidle")

    html = page.content()
    print(html[:2000])

    browser.close()