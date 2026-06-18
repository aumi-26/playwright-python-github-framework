from time import time

from playwright.sync_api import Page, expect


def test_UIvalidationDynamicScript(page: Page, locator=None):
    # iphone x, nokia edge are showing correctly
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("button", name="Sign In").click()
    iphonefinder = page.locator("app-card").filter(has_text= "iphone X")
    iphonefinder.get_by_role("button").click()
    nokiafinder = page.locator("app-card").filter(has_text="Nokia Edge")
    nokiafinder.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").filter(has_text= "Free Access to InterviewQues/ResumeAssistance/Material").click()
        childPage = newPage_info.value
        textOutput = childPage.locator(".red").text_content()
        print(textOutput)
        email = textOutput.split("at")[1].split("with")[0].strip()
        assert email == "mentor@rahulshettyacademy.com"
        #print(email)