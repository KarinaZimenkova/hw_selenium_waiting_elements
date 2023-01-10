import pytest

from sources.page_objects.catalog_page import CatalogPage
from sources.common import create_prerequisites_storage

import time


def test_check_catalog(test_setup, browser):

    t = test_setup

    t.catalog_page.find_desktop_title()

    t.catalog_page.find_product_image(url=browser.url)

    t.catalog_page.switch_to_list_view()

    t.catalog_page.add_to_wish_list()

    t.catalog_page.check_alert_for_unauthorized_user()


@pytest.fixture(scope='function')
def test_setup(browser):

    catalog_page = CatalogPage(browser)
    catalog_page.open(browser.url)

    prerequisites = create_prerequisites_storage()
    prerequisites.catalog_page = catalog_page

    yield prerequisites
