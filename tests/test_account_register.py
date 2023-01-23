import pytest
from faker import Faker
from selenium.webdriver.common.alert import Alert

from sources.page_objects.register_page import RegisterPage
from sources.page_objects.admin_page import AdminPage
from sources.common import create_prerequisites_storage


def test_register_new_account(test_setup, browser):

    t = test_setup
    t.is_new_user = True

    t.register_page.input_firstname(firstname=t.firstname)

    t.register_page.input_lastname(lastname=t.lastname)

    t.register_page.input_email(email=t.email)

    t.register_page.input_msisdn(msisdn=t.msisdn)

    t.register_page.input_password_with_confirm(password=t.password)

    t.register_page.click_acceptance_of_newsletter()

    t.register_page.click_privacy_policy()

    t.register_page.continue_register()

    t.register_page.find_success_registration_header()

    t.register_page.continue_after_success_registration()

    t.admin_page.open(browser.url)
    t.admin_page.login(username='user', password='bitnami')

    t.admin_page.view_customers()

    t.admin_page.filter_by_fullname(fullname=t.fullname)

    assert t.fullname == t.admin_page.fullname_in_first_entry(), \
        f"Не найден новый пользователь. Fullname: {t.fullname}, email: {t.email} "


def test_check_account_register(test_setup):

    t = test_setup

    t.register_page.find_header()

    t.register_page.find_input_for_firstname()

    t.register_page.find_input_for_lastname()

    t.register_page.find_acceptance_of_newsletter()

    t.register_page.find_privacy_policy()


@pytest.fixture(scope='function')
def test_setup(browser):

    is_new_user = False

    register_page = RegisterPage(browser)
    register_page.open(browser.url)

    admin_page = AdminPage(browser)

    fake = Faker()
    fullname = fake.name()
    firstname, lastname = fullname.split(' ')
    email = fake.email()
    msisdn = fake.msisdn()
    password = fake.password()

    prerequisites = create_prerequisites_storage()
    prerequisites.register_page = register_page
    prerequisites.firstname = firstname
    prerequisites.lastname = lastname
    prerequisites.fullname = fullname
    prerequisites.email = email
    prerequisites.msisdn = msisdn
    prerequisites.password = password
    prerequisites.is_new_user = is_new_user
    prerequisites.admin_page = admin_page

    yield prerequisites

    if prerequisites.is_new_user:
        prerequisites.admin_page.select_all_customers()
        prerequisites.admin_page.delete_products()
        Alert(browser).accept()
