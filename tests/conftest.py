import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path='C:\\pythonfiles\\chromedriver.exe')
    options = Options()
    options.headless = False
    options.add_experimental_option("detach", True)
    driver_instance = webdriver.Chrome(service=service, options=options)
    driver_instance.get('https://www.saucedemo.com/')
    driver_instance.implicitly_wait(2)
    yield driver_instance
    # driver_instance.quit()