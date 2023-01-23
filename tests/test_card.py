import pytest

from sources.page_objects.card_page import CardPage
from sources.common import create_prerequisites_storage


def test_check_card(test_setup, browser):

    t = test_setup

    t.card_page.expand_list_of_colors()

    t.card_page.choose_red_color()

    t.card_page.add_product_to_shopping_cart()

    t.card_page.expand_shopping_cart()

    t.card_page.remove_product_from_shopping_cart()


@pytest.fixture(scope='function')
def test_setup(browser):

    card_page = CardPage(browser)
    card_page.open(browser.url)

    prerequisites = create_prerequisites_storage()
    prerequisites.card_page = card_page

    yield prerequisites
