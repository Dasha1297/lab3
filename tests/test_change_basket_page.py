from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from pages.change_basket_page import ChangeBasketPage


def test_change_bascket(web_browser):
    page = ChangeBasketPage(web_browser)

    sleep(2)
    page.element.click()
    sleep(2)
    page.backet_button.click()
    sleep(4)
    page.backet_add.click()
    sleep(2)
    page.backet_icon.click()
    sleep(2)
    page.remove_items.click()
    sleep(2)

    assert page.backet_item.count() == 0

