from html import parser

import pytest
from pytest_bdd import given, when, parsers, scenarios, then
from apiBase.api_baseFramework import api_base
from conftest import one_user_credential
from pageObjects import dashboard
from pageObjects.login import LoginClass

scenarios("features/ordertransaction.feature")

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse("Place the item order with {username} and {password}"))
def place_item_order(playwright, username, password, shared_data):
    one_user_credential = {}
    one_user_credential["userEmail"] = username
    one_user_credential["userPassword"] = password
    calling_api_base = api_base()
    orderid = calling_api_base.test_createorder(playwright, one_user_credential)
    shared_data["order_id"] = orderid

@given("the user on landing page")
def user_on_landing_page(browserinstance, shared_data):
    loginpage = LoginClass(browserinstance)
    loginpage.navigate()
    shared_data['login_page'] = loginpage

@when(parsers.parse("I log in to portal with {username} and {password}"))
def login_to_portal(username, password, shared_data):
    loginpage = shared_data['login_page']
    dashboard = loginpage.login(username, password)
    shared_data['dashboard_page'] = dashboard

@when("navigate to order page")
def navigate_to_orderpage(shared_data):
    dashboard = shared_data['dashboard_page']
    orderHistoryClass = dashboard.selectOrdersNav()
    shared_data['orderHistory_page'] = orderHistoryClass


@when("select the order")
def select_to_order(shared_data):
    orderHistoryClass = shared_data["orderHistory_page"]
    orderid = shared_data["order_id"]
    orderDetailsPage = orderHistoryClass.selectingorder(orderid)
    shared_data['orderDetails_page'] = orderDetailsPage

@then("order message is successfully displayed")
def order_successful_message(shared_data):
    orderDetailsPage = shared_data["orderDetails_page"]
    orderDetailsPage.verifymessage()

