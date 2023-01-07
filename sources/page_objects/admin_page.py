from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sources import admin_css_selectors_lib as css_selectors


class AdminPage:
    path = "/admin"

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + self.path)

    def find_input_for_username(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                              css_selectors.USERNAME)))

    def find_input_for_password(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                              css_selectors.PASSWORD)))

    def submit_login(self):
        self.driver.find_element(By.CSS_SELECTOR, css_selectors.LOGIN_BTN).click()

    def check_warning_message(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, css_selectors.LOGIN_BTN)))

    def find_forgotten_password_btn(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, css_selectors.FORGOTTEN_LOGIN_BTN)))
