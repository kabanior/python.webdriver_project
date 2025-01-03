from selenium.webdriver.common.by import By


class CheckOutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver

    def finish_button_click (self):
        finish_button = self.driver.find_element(By.XPATH, "//button[@data-test='finish']")
        finish_button.click()