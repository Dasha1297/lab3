from time import sleep
import pytest
from pages.navigation_page import NavigationPage


def test_navigation(web_browser):

    page = NavigationPage(web_browser)

    page.interior.click()
    sleep(2)
    assert page.get_current_url().startswith(
        'https://krasdivan.shop/catalog/gotovie%20/')

    page.go_back()
    sleep(2)

    page.sofas.click()
    sleep(2)
    assert  page.get_current_url().startswith(
        'https://krasdivan.shop/catalog/divany_i_kresla/')

    # page.go_back()
    # sleep(2)
    #
    # page.livingRoom.click()
    # sleep(2)
    # assert page.get_current_url().startswith(
    #     'https://krasdivan.shop/catalog/mebel_dlya_gostinoy/')
    #
    # page.go_back()
    # sleep(2)
    #
    # page.bedroom.click()
    # sleep(2)
    # assert  page.get_current_url().startswith(
    #     'https://krasdivan.shop/catalog/tovary_dlya_spalni/')
    #
    # page.go_back()
    # sleep(2)
    #
    # page.childrensRoom.click()
    # sleep(2)
    # assert  page.get_current_url().startswith(
    #     'https://krasdivan.shop/catalog/mebel_dlya_detskoy/')
    #
    # page.go_back()
    # sleep(2)
    # page.hallway.click()
    # sleep(2)
    # assert  page.get_current_url().startswith(
    #     'https://krasdivan.shop/catalog/mebel_dlya_prikhozhey/')


