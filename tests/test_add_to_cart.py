from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("sauce-labs-backpack")
    inventory_page.go_to_cart()