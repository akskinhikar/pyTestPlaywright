from playwright.sync_api import Playwright

create_order_payload = {"orders": [{"country": "India", "productOrderedId": "67a8df1ac0d3e6622a297ccb"}]}
login_payload = {"userEmail": "akskinhikar@gmail.com", "userPassword": "Akshay@21"}


class APIUtils:

    def get_token_for_login(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/auth/login",
                                 data=login_payload)
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]


    def create_order(self,playwright: Playwright):
        token = self.get_token_for_login(playwright)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("api/ecom/order/create-order",
                                 data= create_order_payload,
                                 headers={"Authorization": token,
                                          "Content-Type":"application/json"
                                          })

        print(response.json())
        response_body = response.json()
        return response_body["orders"][0]
