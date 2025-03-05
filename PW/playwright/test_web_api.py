from playwright.sync_api import Playwright, expect
from PW.utils.apiBase import APIUtils


def test_e2e_web_api(playwright:Playwright):
    global view_index
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Create Order using API
    api_util = APIUtils()
    order_no = api_util.create_order(playwright)
    print(order_no)

    #Login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("akskinhikar@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Akshay@21")
    page.get_by_role("button",name="Login").click()

    #orders history
    page.get_by_role("button",name="ORDERS").click()
    order_id_row = page.locator("tr").filter(has_text=order_no)
    order_id_row.get_by_role("button", name = "View").click()
    expect(page.locator("//p[@class='tagline']")).to_contain_text("Thank you for Shopping With Us")
    expect(page.get_by_text("Thank you for Shopping With Us")).to_be_visible()
    context.close()






