import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_catalog(test_setup, browser):

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[title=Desktops]")))

    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, f"[src='{browser.url}/image/cache/catalog/demo/apple_cinema_30-228x228.jpg']")))

    WebDriverWait(browser, 2).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, "button#list-view.btn.btn-default")))

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located(((
        By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")))).click()

    WebDriverWait(browser, 2).until(EC.visibility_of_element_located(((
        By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible"))))


@pytest.fixture(scope='function')
def test_setup(browser):
    desktops_url = browser.url + "/desktops"
    browser.get(desktops_url)
