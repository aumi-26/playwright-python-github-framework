from pageObjects.dashboard import DashboardPage


class LoginClass:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self,user_mail, user_password):
        self.page.get_by_placeholder("email@example.com").fill(user_mail)
        self.page.get_by_placeholder("enter your passsword").fill(user_password)
        self.page.get_by_role("button", name="Login").click()
        dashboard = DashboardPage(self.page)
        return dashboard