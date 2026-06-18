from pageObjects.ordre_history import OrderHistoryClass


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def selectOrdersNav(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderHistoryClass = OrderHistoryClass(self.page)
        return orderHistoryClass