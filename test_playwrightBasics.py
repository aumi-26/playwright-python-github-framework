import time
from playwright.sync_api import Page, expect, Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

def test_playwrightShortcut(page:Page):
    page.goto("https://rahulshettyacademy.com")

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learningd@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    # Incorrect username/password.
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    # dont need to wait as i give waiting assertion
    # time.sleep(10)


def test_firefoxBrowser(playwright):
    browserfirefox = playwright.firefox.launch(headless=False)
    page = browserfirefox.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learningd@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name = "terms and conditions").click()
    # Incorrect username/password.
    page.get_by_role("button", name = "Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    # dont need to wait as i give waiting assertion
    # time.sleep(10)