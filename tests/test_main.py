from sources.page_objects.main_page import MainPage


def test_check_main(browser):

    main_page = MainPage(browser)

    main_page.find_logo()

    main_page.view_shopping_cart()

    main_page.find_text_in_shopping_cart()

    main_page.find_total_wish_list()

    main_page.find_search_block()
