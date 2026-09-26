from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def browser():
 browser= webdriver.Chrome()
 browser.maximize_window()
 browser.implicitly_wait(60)
 yield browser

def test_open_page(browser):
    browser.get("https://demoblaze.com/")
    galaxy_s6 =browser.find_element(By.XPATH, value='//a[text()="Samsung galaxy s6"]')
    galaxy_s6.click()
    title= browser.find_element(By.CSS_SELECTOR, "h2")
    assert title.text=="Samsung galaxy s6"

def test_monitors(browser):
    browser.get("https://demoblaze.com/")
    monitor_link= browser.find_element(By.CSS_SELECTOR, value='''[onclick="byCat('monitor')"]''')
    monitor_link.click()
    time.sleep(4)
    monitors = browser.find_elements(By.CSS_SELECTOR, value='.card')
    assert len(monitors)==2