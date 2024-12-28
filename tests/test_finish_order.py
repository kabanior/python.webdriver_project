from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckOutStepOne
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.checkout_step_two_page import CheckOutStepTwo


def test_checkout(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.go_to_checkout()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    checkout_page = CheckOutStepOne(driver)
    checkout_page.enter_checkout_info("Polska mistrzem", "Polski", "1906")
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    finish_order = CheckOutStepTwo(driver)
    finish_order.finish_button_click()
    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html"