from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_checkout(self):
        checkout_button = self.driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout_button.click()

    def remove_product(self, product_name):
        remove_button = self.driver.find_element(By.XPATH, f"//button[@data-test='remove-{product_name}']")
        remove_button.click()
