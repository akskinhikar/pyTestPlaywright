from PW.pageobjects.orderhistory import OrderHistoryPage


class DashboardPage:
    def __init__(self,page):
        self.page = page

    def select_orders_navigation_link(self):
        self.page.get_by_role("button", name="ORDERS").click()
        order_history = OrderHistoryPage(self.page)
        return order_history


