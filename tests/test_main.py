from currency_converter import CurrencyConverter
from sources.page_objects.main_page import MainPage

import time


def test_check_main(browser):

    main_page = MainPage(browser)

    main_page.find_logo()

    main_page.view_shopping_cart()

    main_page.find_text_in_shopping_cart()

    main_page.find_total_wish_list()

    main_page.find_search_block()


def test_change_currency(browser):

    main_page = MainPage(browser)

    main_page.add_product_to_shopping_cart()
    assert "$" in main_page.get_currency_in_shopping_cart(), "Итоговая сумма в корзине не в $"

    main_page.view_list_of_currencies()

    main_page.select_eur()
    assert "€" in main_page.get_currency_in_shopping_cart(), "Итоговая сумма в корзине не в €"

    main_page.view_list_of_currencies()

    main_page.select_gbp()
    assert "£" in main_page.get_currency_in_shopping_cart(), "Итоговая сумма в корзине не в £"
