from playwright.sync_api import Playwright, expect
from pytest_playwright.pytest_playwright import context

from apiBase.api_base import api_base


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Create Order > OrderID
    calling_api_base = api_base()
    orderid = calling_api_base.test_createorder(playwright)

    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("aumisky18@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Testing@18")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()

    # Order history
    row = page.locator("tr").filter(has_text=orderid)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    context.close()