import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_card(test_setup, browser):

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-option226"))).click()

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                      "#input-option226 > option:nth-child(2)"))
                                    ).click()

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                      "#button-cart"))).click()

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                      "#cart"))).click()

    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#cart > ul > li:nth-child(1) > table > tbody > tr > td:nth-child(5) > button"))).click()


@pytest.fixture(scope='function')
def test_setup(browser):
    desktops_url = browser.url + "/desktops/canon-eos-5d"
    browser.get(desktops_url)
