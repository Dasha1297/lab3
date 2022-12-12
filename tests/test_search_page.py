from time import sleep
import pytest
from selenium.webdriver.common.keys import Keys
from pages.search_page import SearchPage


def test_search(web_browser):

    page = SearchPage(web_browser)
    page.search_input.click()
    page.search_input.send_keys('Подушка Маттео')
    sleep(2)
    page.btn.click()
    assert page.goods.count()  == 11

    # for good in page.goods.get_text():
    #     msg = 'Wrong product in search "{}"'.format(good)
    #     assert 'Подушка Маттео' in good.lower(), msg

