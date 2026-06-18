import pytest
from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

    # Checking page text when no order in the page
def intercept_response(route):
    route.fulfill(json=fakePayloadOrderResponse)

@pytest.mark.smoke
def test_network_1(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.get_by_placeholder("email@example.com").fill("aumisky18@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Testing@18")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text = page.locator(".mt-4").get_by_text(" You have No Orders to show at this time.")
    assert order_text