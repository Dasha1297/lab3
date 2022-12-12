from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class FilterPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://krasdivan.shop/catalog/?q=%D0%B4%D0%B8%D0%B2%D0%B0%D0%BD-%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%84%D0%BE%D1%80%D0%BC%D0%B5%D1%80'
        super().__init__(web_driver, url)

    goods = ManyWebElements(class_name="product-card")
    filter_input = WebElement(id='searchFilter_P1_MAX')
    btn = WebElement(name='set_filter')
