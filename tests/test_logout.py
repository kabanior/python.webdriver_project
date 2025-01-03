from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    menu = driver.find_element(By.XPATH, "//button[@id='react-burger-menu-btn']")
    menu.click()
    logout_button = driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link']")
    logout_button.click()
    assert driver.current_url == "https://www.saucedemo.com/"
    assert driver.find_element(By.XPATH, "//input[@id='login-button']").is_displayed() == True