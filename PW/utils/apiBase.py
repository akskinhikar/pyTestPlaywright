from playwright.sync_api import Playwright

create_order_payload = {"orders": [{"country": "India", "productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}


class APIUtils:

    def get_token_for_login(self,playwright:Playwright,user_creds):
        userName = user_creds["user_email"]
        password = user_creds["password"]
        login_payload = {"userEmail": userName, "userPassword": password}

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/auth/login",
                                 data=login_payload)
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]


    def create_order(self,playwright: Playwright,user_creds):
        token = self.get_token_for_login(playwright,user_creds)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/order/create-order",
                                 data= create_order_payload,
                                 headers={"Authorization": token,
                                          "Content-Type":"application/json"
                                          })

        print(response.json())
        response_body = response.json()
        return response_body["orders"][0]
