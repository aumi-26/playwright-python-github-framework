from playwright.sync_api import Page, Playwright, expect

from apiBase.api_base import api_base


    # Unapproving to see other order
def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6711e249ae2afd4c0b9f6fb0")

def test_network_2(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder("email@example.com").fill("aumisky18@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Testing@18")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)


    # Login with token id
def test_session_storage(playwright: Playwright):
    session_var = api_base()

    token = session_var.getToken(playwright)

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.add_init_script(
        f"localStorage.setItem('token', '{token}')"
    )

    page.goto("https://rahulshettyacademy.com/client")

    page.get_by_role("button", name="ORDERS").click()

    expect(page.get_by_text("Your Orders")).to_be_visible()