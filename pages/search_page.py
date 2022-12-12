from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class SearchPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://krasdivan.shop'
        super().__init__(web_driver, url)

    search_input = WebElement(id='title-search-input')
    btn = WebElement(class_name="icon-custom")
    goods = ManyWebElements(
        class_name="product-wrap")
