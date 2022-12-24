import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_login(test_setup, browser):

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-username")))

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                      "#input-password")))

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
         "#content > div > div > div > div > div.panel-body > form > div.text-right > button"))).click()

    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR,
         "#content > div > div > div > div > div.panel-body > div > i")))

    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a")))


@pytest.fixture(scope='function')
def test_setup(browser):
    desktops_url = browser.url + "/admin"
    browser.get(desktops_url)
