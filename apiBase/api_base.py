from playwright.sync_api import Playwright

orders_payload = {"orders":[{"country":"Bangladesh","productOrderedId":"6960ea76c941646b7a8b3dd5"}]}



class api_base:

    def getToken(self, playwright: Playwright):

        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                 data={"userEmail": "aumisky18@gmail.com",  "userPassword": "Testing@18"})
        assert response.ok
        print(response.json())
        response_body = response.json()
        return response_body["token"]


    def test_createorder(self, playwright: Playwright):
        token = self.getToken(playwright)
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
 