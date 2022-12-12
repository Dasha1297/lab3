from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class BasketPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://krasdivan.shop/catalog/divany_i_kresla/'
        super().__init__(web_driver, url)

    element = WebElement(
        xpath='/html/body/div[2]/div[2]/div[2]/div/main/div[4]/div[2]/div[1]/div[1]/div/div/div[1]/div[3]/a[2]')

    backet_button = WebElement(xpath='/html/body/div[11]/div/div[3]/div[4]/div/div[2]/div[1]/a[1]')

    backet_add = WebElement(xpath='/html/body/div[2]')
    backet_icon = WebElement(xpath='/html/body/div[2]/header/div[2]/div/div[5]/div/a')

    backet_item =  ManyWebElements(xpath='/html/body/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/table/tbody/tr')