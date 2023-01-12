import pytest

from sources.page_objects.admin_page import AdminPage
from sources.common import create_prerequisites_storage

import time


def test_check_login(test_setup):

    t = test_setup

    t.admin_page.find_input_for_username()

    t.admin_page.find_input_for_password()

    t.admin_page.submit_login()

    t.admin_page.check_warning_message()

    t.admin_page.find_forgotten_password_btn()


def test_add_new_product(test_setup):

    t = test_setup

    t.admin_page.input_username(username="user")

    t.admin_page.input_password(password="bitnami")

    t.admin_page.submit_login()

    t.admin_page.click_to_catalog()

    t.admin_page.view_products()

    t.admin_page.add_product()

    t.admin_page.input_product_name(product_name="Монитор DELL 27URTY")

    t.admin_page.input_meta_tag_title(tag_title="Мониторы")

    t.admin_page.switch_to_data_in_product_profile()

    t.admin_page.input_model(model="27URTY")

    t.admin_page.save_product()

    #t.admin_page.get_alert_about_success_saved_product()

    #assert 'Success: You have modified products!×' == t.admin_page.get_alert_about_success_saved_product(), \
    #    "Текст в алерте не соотвествует ожидаемому при добавлении нового товара"

    t.admin_page.filter_by_product_name(product_name="Монитор DELL 27URTY")

    t.admin_page.filter_products()

    assert "Монитор DELL 27URTY" == t.admin_page.get_model_name()

    time.sleep(5)


@pytest.fixture(scope='function')
def test_setup(browser):

    admin_page = AdminPage(browser)
    admin_page.open(browser.url)

    prerequisites = create_prerequisites_storage()
    prerequisites.admin_page = admin_page

    yield prerequisites
