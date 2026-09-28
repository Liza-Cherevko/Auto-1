import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_add_to_card(browser, test_login):
    product = browser.find_element(
        By.XPATH, "//div[text()='Sauce Labs Backpack']"
    )

    add_to_card = browser.find_element(
        By.ID, 'add-to-cart-sauce-labs-backpack'
    )

    add_to_card.click()
    print('товар добавлен')

    shopping_card_container = browser.find_element(
        By.ID, 'shopping_cart_container'
    )
    shopping_card_container.click()
    print('зашла в корзину')

    # Заново ищем товар уже в корзине
    product_in_cart = browser.find_element(
        By.XPATH, "//div[text()='Sauce Labs Backpack']"
    )

    assert product_in_cart.text == 'Sauce Labs Backpack'
