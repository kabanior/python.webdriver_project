from selenium.webdriver.common.by import By

from pages.login_page import LoginPage

def test_failed_login(driver):
    login_page = LoginPage(driver)
    login_page.login("qwe", "qwe")
    assert driver.current_url == "https://www.saucedemo.com/"
    assert driver.find_element(By.XPATH, "//h3[@data-test='error']").text == "Epic sadface: Username and password do not match any user in this service"