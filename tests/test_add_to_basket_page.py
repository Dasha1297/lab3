from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from pages.add_to_basket_page import BasketPage

def test_add_to_bascket(web_browser):
    page = BasketPage(web_browser)

    sleep(2)
    page.element.click()
    sleep(2)
    page.backet_button.click()
    sleep(4)
    page.backet_add.click()
    sleep(2)
    page.backet_icon.click()
    sleep(2)


    assert page.backet_item.count() >= 1