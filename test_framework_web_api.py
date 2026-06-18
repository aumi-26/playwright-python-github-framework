import json

import pytest
from playwright.sync_api import Playwright, expect

from apiBase.api_baseFramework import api_base
from pageObjects.dashboard import DashboardPage
from pageObjects.login import LoginClass
from pageObjects import dashboard

# JSON File opening
with open('data_json/credentials.json') as f:
    test_obj_dict = json.load(f)
    print(test_obj_dict)
    test_obj_list = test_obj_dict["user_details"]

@pytest.mark.smoke
@pytest.mark.parametrize('one_user_credential', test_obj_list)
def test_e2e_web_api(playwright: Playwright, browserinstance, one_user_credential):
    user_mail = one_user_credential["userEmail"]
    user_password = one_user_credential["userPassword"]


    # Create Order > OrderID
    calling_api_base = api_base()
    orderid = calling_api_base.test_createorder(playwright, one_user_credential)

    # Login Page
    loginpage = LoginClass(browserinstance)
    loginpage.navigate()
    dashboard = loginpage.login(user_mail, user_password)

    # Dashboard Page
    orderHistoryClass = dashboard.selectOrdersNav()
    orderDetailsPage = orderHistoryClass.selectingorder(orderid)
    orderDetailsPage.verifymessage()
    # Order history


