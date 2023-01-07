import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_account_register(test_setup, browser):

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#content > h1")))

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-firstname")))

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-lastname")))

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
         "#content > form > fieldset:nth-child(3) > div > div > label:nth-child(2) > input[type=radio]")))

    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)")))


@pytest.fixture(scope='function')
def test_setup(browser):
    desktops_url = browser.url + "/index.php?route=account/register"
    browser.get(desktops_url)
