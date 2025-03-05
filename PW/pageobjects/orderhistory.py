from PW.pageobjects.orderdetails import OrderDetailsPage


class OrderHistoryPage:
    def __init__(self,page):
        self.page = page

    def selecting_order(self, order_no):
        order_id_row = self.page.locator("tr").filter(has_text=order_no)
        order_id_row.get_by_role("button", name="View").click()
        order_details_page = OrderDetailsPage(self.page)
        return order_details_page
