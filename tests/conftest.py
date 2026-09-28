import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get('https://www.saucedemo.com/')
    print('Browser opened')
    browser.implicitly_wait(60)
    yield browser
    print('Browser closed')


@pytest.fixture(scope="session")
def test_login( browser):
    user_name = browser.find_element(By.ID, 'user-name')
    user_name.send_keys('standard_user')
    password = browser.find_element(By.ID, 'password')
    password.send_keys('secret_sauce')
    login_button=browser.find_element(By.ID,'login-button')
    login_button.click()
    print('Login success')
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'