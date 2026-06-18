from pageObjects.order_details import OrderDetailsPage


class OrderHistoryClass:
    def __init__(self, page):
        self.page = page

    def selectingorder(self, orderid):
        row = self.page.locator("tr").filter(has_text=orderid)
        row.get_by_role("button", name="View").click()
        orderDetailsPage = OrderDetailsPage(self.page)
        return orderDetailsPage