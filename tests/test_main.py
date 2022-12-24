from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_check_main(browser):

    WebDriverWait(browser, 1).until(EC.visibility_of(browser.find_element_by_id('logo')))

    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "button.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle"))).click()

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.text-center")))

    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a#wishlist-total")))

    WebDriverWait(browser, 1).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#search")))

