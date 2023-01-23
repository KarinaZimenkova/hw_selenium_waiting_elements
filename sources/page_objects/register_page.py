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

    def input_firstname(self, firstname):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.FIRSTNAME)).send_keys(firstname)

    def find_input_for_lastname(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.LASTNAME))

    def input_lastname(self, lastname):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.LASTNAME)).send_keys(lastname)

    def input_email(self, email):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.EMAIL)).send_keys(email)

    def input_msisdn(self, msisdn):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.MSISDN)).send_keys(msisdn)

    def input_password_with_confirm(self, password):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.PASSWORD)).send_keys(password)
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.PASSWORD_CONFIRM)
                                            ).send_keys(password)

    def find_acceptance_of_newsletter(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.ACCEPTANCE_OF_NEWSLETTER))

    def click_acceptance_of_newsletter(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.ACCEPTANCE_OF_NEWSLETTER)).click()

    def find_privacy_policy(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.PRIVACY_POLICY))

    def click_privacy_policy(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.PRIVACY_POLICY)).click()

    def continue_register(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.CONTINUE_BTN)).click()

    def find_success_registration_header(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
            locators.SUCCESS_REGISTRATION_HEADER)).text

    def continue_after_success_registration(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(
            locators.CONTINUE_BTN_AFTER_SUCCESS_REGISTRATION)).click()

    def edit_account(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.EDIT_ACCOUNT)).click()
