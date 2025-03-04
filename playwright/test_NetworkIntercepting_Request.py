import time

from playwright.sync_api import Page


fake_order_id_url = "https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=67c778dfc019fb1ad616a1az"

def test_Network_2(page:Page):
    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", lambda route:route.continue_(url=fake_order_id_url))
    page.get_by_placeholder("email@example.com").fill("akskinhikar@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Akshay@21")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button",name="View").first.click()
    message = page.locator(".blink_me").text_content()
    print(message)






