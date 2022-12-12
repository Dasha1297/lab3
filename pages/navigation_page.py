from pages.base import WebPage
from pages.elements import WebElement


class NavigationPage(WebPage):
    def __init__(self, web_driver, url=''):
        url = 'https://krasdivan.shop/'
        super().__init__(web_driver, url)

    interior = WebElement(
        xpath='/html/body/div/aside/div/nav/div[3]/ul/div/div/li[1]/a'
    )

    sofas = WebElement(
        xpath='/html/body/div/aside/div/nav/div[3]/ul/div/div/li[2]/a')

    computers = WebElement(
        xpath='/html/body/div/aside/div/nav/div[3]/ul/div/div/li[3]/a')

    livingRoom = WebElement(
       xpath='/html/body/div/aside/div/nav/div[3]/ul/div/div/li[4]/a')

    bedroom = WebElement(
        xpath='/html/body/div/aside/div/nav/div[3]/ul/div/div/li[5]/a')

    childrensRoom = WebElement(
       xpath='/html/body/div/aside/div/nav/div[3]/ul/div/div/li[6]/a')

    hallway = WebElement(
       xpath='/html/body/div/aside/div/nav/div[3]/ul/div/div/li[7]/a')

