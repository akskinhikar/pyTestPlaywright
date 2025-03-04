from playwright.sync_api import Page


fake_payload_order_response = {"data": [], "message": "No Orders"}
def test_Network_1(page:Page):
    # Login
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", lambda route: route.fulfill(json=fake_payload_order_response))
    page.get_by_placeholder("email@example.com").fill("akskinhikar@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Akshay@21")
    page.get_by_role("button", name="Login").click()

    # orders history
    page.get_by_role("button", name="ORDERS").click()
    text_value = page.locator(".mt-4").text_content()
    print(text_value)



