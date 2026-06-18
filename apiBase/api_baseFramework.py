from playwright.sync_api import Playwright

orders_payload = {"orders":[{"country":"Bangladesh","productOrderedId":"6960ea76c941646b7a8b3dd5"}]}



class api_base:

    def getToken(self, playwright: Playwright, one_user_credential):
        user_mail_value = one_user_credential["userEmail"]
        user_password_value = one_user_credential["userPassword"]
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": user_mail_value, "userPassword": user_password_value})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]


    def test_createorder(self, playwright: Playwright, one_user_credential):
        token = self.getToken(playwright, one_user_credential)
        api_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response = api_context.post("/api/ecom/order/create-order",
                         data=orders_payload,
                         headers={"Authorization": token,
                                    "Content-type" : "application/json"})

        print(response.json())
        response_body = response.json()
        orderid = response_body["orders"][0]
        print("This is order id : "+orderid)
        return orderid
 