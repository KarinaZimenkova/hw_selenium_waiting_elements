import pytest

from sources.page_objects.admin_page import AdminPage
from sources.common import create_prerequisites_storage


def test_check_login(test_setup):

    t = test_setup

    t.admin_page.find_input_for_username()

    t.admin_page.find_input_for_password()

    t.admin_page.submit_login()

    t.admin_page.check_warning_message()

    t.admin_page.find_forgotten_password_btn()


@pytest.fixture(scope='function')
def test_setup(browser):

    admin_page = AdminPage(browser)
    admin_page.open(browser.url)

    prerequisites = create_prerequisites_storage()
    prerequisites.admin_page = admin_page

    yield prerequisites
