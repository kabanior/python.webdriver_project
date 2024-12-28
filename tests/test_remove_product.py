from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_checkout(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.remove_product("sauce-labs-backpack")
    try:
        driver.find_element(By.XPATH, "//div[@data-test='inventory-item']")
        assert False, "Test failed: element exist"
    except NoSuchElementException:
        assert True
        print("Test passed: Element do not exist")