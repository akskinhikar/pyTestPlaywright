from os.path import split
from playwright.sync_api import Page, expect


def test_ui_validation_dynamic_script(page: Page):
    #iphoneX, Nokia Edge
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    #will get iphone x product added to cart
    iphone_prod = page.locator("app-card").filter(has_text="iphone X")
    iphone_prod.get_by_role("button").click()
    # will get nokia edge product added to cart
    nokia_edge_prod = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_edge_prod.get_by_role("button").click()
    #validate item count in cart
    page.get_by_text("Checkout").click()
    expect(page.locator(".media-body")).to_have_count(2)

def test_child_window_handle(page : Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click()
        new_page = newPage_info.value
        text = new_page.locator(".red").text_content()
        #print(text)
        word = text.split("at ")
        email =  word[1].split(" ")[0]
        assert email == "mentor@rahulshettyacademy.com"






