from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sources.elements.register_locators import RegisterPageLocators as locators


class RegisterPage:
    path = "/index.php?route=account/register"

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + self.path)

    def find_header(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.HEADER))

    def find_input_for_firstname(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.FIRSTNAME))

    def find_input_for_lastname(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.LASTNAME))

    def find_acceptance_of_newsletter(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.ACCEPTANCE_OF_NEWSLETTER))

    def find_privacy_policy(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.PRIVACY_POLICY))
