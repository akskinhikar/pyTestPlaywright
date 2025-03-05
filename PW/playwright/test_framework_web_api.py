import json
import pytest
from playwright.sync_api import Playwright
from PW.pageobjects.login import LoginPage
from PW.utils.apiBase import APIUtils

# JSON file --> Util file --> Convert it into Python object --> Access into test
with open('../data/cred.json') as f:
    test_data = json.load(f)
    user_creds_list = test_data['user_credentials']

@pytest.mark.parametrize('user_creds', user_creds_list)
def test_e2e_web_api(playwright:Playwright, user_creds):
    global view_index
    user_name = user_creds["user_email"]
    password = user_creds["password"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #Create Order using API
    api_util = APIUtils()
    order_no = api_util.create_order(playwright,user_creds)
    print(order_no)

    #Login
    login_page = LoginPage(page)
    login_page.navigate()
    dashboard_page = login_page.login(user_name,password)

    #orders history
    order_history_page = dashboard_page.select_orders_navigation_link()
    order_details_page = order_history_page.selecting_order(order_no)
    order_details_page.verify_order_message()


    context.close()






