from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        add_button = self.driver.find_element(By.XPATH, f"//button[@data-test='add-to-cart-{product_name}']")
        add_button.click()

    def go_to_cart(self):
        cart_link = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()