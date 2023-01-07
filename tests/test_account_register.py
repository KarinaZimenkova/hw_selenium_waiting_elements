import pytest

from sources.page_objects.register_page import RegisterPage
from sources.common import create_prerequisites_storage


def test_check_account_register(test_setup, browser):

    t = test_setup

    t.register_page.find_header()

    t.register_page.find_input_for_firstname()

    t.register_page.find_input_for_lastname()

    t.register_page.find_radio_btn()

    t.register_page.find_checkbox()


@pytest.fixture(scope='function')
def test_setup(browser):
    register_page = RegisterPage(browser)
    register_page.open(browser.url)

    prerequisites = create_prerequisites_storage()
    prerequisites.register_page = register_page

    yield prerequisites
