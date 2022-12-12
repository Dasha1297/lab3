from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://krasdivan.shop/auth/'
        super().__init__(web_driver, url)

    telephone = WebElement(name='USER_LOGIN')

    password = WebElement(name='USER_PASSWORD')

    btn = WebElement(name='Login')
