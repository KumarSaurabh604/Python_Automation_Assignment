import time
import pytest
from pytest_bdd import given, when, then, scenario, parsers
from uibddpytest.pages.cart_page import CartPage
from uibddpytest.pages.Base import GetDataFromFile
from uibddpytest.pages.home_page import HomePage
from uibddpytest.pages.product_page import ProductPage
from uibddpytest.pages.search_results_page import SearchResultsPage


@scenario('../uibddpytest/myFeatures/item_ordering.feature', 'Add two items to the cart and verify cart contents and total price')
def test_Search():
    pass


@pytest.mark.usefixtures("browser")
@given('User open the Flipkart website')
def open_flipkart(browser):
    browser.get("https://www.flipkart.com/")


@when(parsers.parse('User search for {item} and select the second item'))
def search_and_select_second_item(browser, item):
    home_page = HomePage(browser)
    home_page.search_for_item(item)
    search_results_page = SearchResultsPage(browser)
    search_results_page.select_second_item(item)


@then(parsers.parse('User check the availability using the pin code {pin} and add {product} it to the cart'))
def check_availability_and_add_to_cart(browser, pin, product):
    product_page = ProductPage(browser)
    product_page.enter_pin_code_and_check_availability(pin, product)
    product_page.add_to_cart()


@then('User return to the home page')
def return_to_home_page(browser):
    home_page = HomePage(browser)
    home_page.navigateToHome()


@then('User navigate to the cart')
def navigate_to_cart(browser):
    home_page = HomePage(browser)
    home_page.closeButton()
    time.sleep(2)
    cart_page = CartPage(browser)
    cart_page.search_for_item()
    time.sleep(2)


@then('User verify that both items are present in the cart')
def verify_cart_contents(browser):
    cart_page = CartPage(browser)
    first_product_name = GetDataFromFile("productPage","first_item")
    assert cart_page.is_item_present(first_product_name)
    first_product_name = GetDataFromFile("productPage", "second_item")
    assert cart_page.is_item_present(first_product_name)


@then('User verify that the total price reflects the sum of both items')
def verify_total_price(browser):
    cart_page = CartPage(browser)
    assert cart_page.verify_total_price()


@then('User remove one item from the cart')
def item_remove(browser):
    cart_page = CartPage(browser)
    product_name = GetDataFromFile("productPage", "second_item")
    cart_page.remove_item(product_name)


@then('User verify that the total price is updated')
def verify_total_price(browser):
    cart_page = CartPage(browser)
    assert cart_page.price_after_removed_item()

