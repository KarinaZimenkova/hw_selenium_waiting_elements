import pytest
from selenium.webdriver.common.alert import Alert

from sources.page_objects.admin_page import AdminPage
from sources.common import create_prerequisites_storage


def test_check_login(test_setup):

    t = test_setup

    t.admin_page.find_input_for_username()

    t.admin_page.find_input_for_password()

    t.admin_page.submit_login()

    t.admin_page.check_warning_message()

    t.admin_page.find_forgotten_password_btn()


def test_add_new_product(test_setup_add_product):

    t = test_setup_add_product

    t.admin_page.click_to_catalog()

    t.admin_page.view_products()

    t.admin_page.add_product()

    t.admin_page.input_product_name(product_name="Монитор DELL 27URTY")

    t.admin_page.input_meta_tag_title(tag_title="Мониторы")

    t.admin_page.switch_to_data_in_product_profile()

    t.admin_page.input_model(model="27URTY")

    t.admin_page.save_product()
    assert 'Success: You have modified products!' in t.admin_page.get_alert_about_success_saved_product(), \
        "Текст в алерте не соотвествует ожидаемому при добавлении нового товара"

    t.admin_page.filter_by_product_name(product_name="Монитор DELL 27URTY")
    t.admin_page.filter_products()
    assert "Монитор DELL 27URTY" == t.admin_page.get_model_name()


def test_delete_product(test_setup_delete_product, browser):

    t = test_setup_delete_product

    t.admin_page.filter_by_product_name(product_name=t.product_name)
    t.admin_page.filter_products()

    t.admin_page.select_first_product()

    t.admin_page.delete_products()
    Alert(browser).accept()
    assert 'Success: You have modified products!' in t.admin_page.get_success_alert(), \
        "Текст в алерте не соответствует ожидаемому при добавлении нового товара"

    t.admin_page.filter_by_product_name(product_name=t.product_name)
    t.admin_page.filter_products()
    assert 'No results!' == t.admin_page.get_products_list(), \
        "Текст в таблице не соответствует ожидаемому при удалении товара"


@pytest.fixture(scope='function')
def test_setup_add_product(browser):

    admin_page = AdminPage(browser)
    admin_page.open(browser.url)

    admin_page.login(username='user', password='bitnami')

    prerequisites = create_prerequisites_storage()
    prerequisites.admin_page = admin_page

    yield prerequisites

    prerequisites.admin_page.select_all_products()
    prerequisites.admin_page.delete_products()
    Alert(browser).accept()


@pytest.fixture(scope='function')
def test_setup_delete_product(browser):

    admin_page = AdminPage(browser)
    admin_page.open(browser.url)

    prerequisites = create_prerequisites_storage()
    prerequisites.admin_page = admin_page
    prerequisites.product_name = "Монитор MSI 115"

    admin_page.login(username='user', password='bitnami')

    admin_page.click_to_catalog()

    admin_page.view_products()

    admin_page.add_product()

    admin_page.input_product_name(product_name=prerequisites.product_name)

    admin_page.input_meta_tag_title(tag_title="Мониторы")

    admin_page.switch_to_data_in_product_profile()

    admin_page.input_model(model="115")

    admin_page.save_product()

    yield prerequisites
