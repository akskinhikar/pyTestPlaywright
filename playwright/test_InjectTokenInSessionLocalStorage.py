from playwright.sync_api import Playwright, expect
from utils.apiBase import APIUtils


def test_session_storage(playwright:Playwright):
    api_utils = APIUtils()
    get_token = api_utils.get_token_for_login(playwright)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{get_token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()
