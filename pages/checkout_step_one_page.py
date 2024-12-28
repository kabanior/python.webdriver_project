from selenium.webdriver.common.by import By


class CheckOutStepOne:
    def __init__(self, driver):
        self.driver = driver

    def enter_checkout_info (self, first_name, last_name, zip_code):
        first_name_input = self.driver.find_element(By.XPATH, "//input[@data-test='firstName']")
        last_name_input = self.driver.find_element(By.XPATH, "//input[@data-test='lastName']")
        zip_code_input = self.driver.find_element(By.XPATH, "//input[@data-test='postalCode']")
        continue_button = self.driver.find_element(By.XPATH, "//input[@type='submit']")

        first_name_input.clear()
        first_name_input.send_keys(first_name)
        last_name_input.clear()
        last_name_input.send_keys(last_name)
        zip_code_input.clear()
        zip_code_input.send_keys(zip_code)
        continue_button.click()