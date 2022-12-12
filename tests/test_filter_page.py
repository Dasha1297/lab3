from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from pages.filter_page import FilterPage


def test_filter(web_browser):

    page = FilterPage(web_browser)
    page.filter_input.send_keys('60000')
    sleep(2)
    page.btn.click()
    sleep(2)


    assert page.goods.count() == 4
