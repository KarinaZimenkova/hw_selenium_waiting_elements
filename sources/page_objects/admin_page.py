from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sources.elements.admin_locators import AdminPageLocators as locators


class AdminPage:
    path = "/admin"

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + self.path)

    def find_input_for_username(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.USERNAME))

    def input_username(self, username):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.USERNAME)).click()
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.USERNAME)).send_keys(username)

    def find_input_for_password(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.PASSWORD))

    def input_password(self, password):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.PASSWORD)).click()
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.PASSWORD)).send_keys(password)

    def submit_login(self):
        self.driver.find_element(By.CSS_SELECTOR, locators.LOGIN_BTN).click()

    def click_to_catalog(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.CATALOG)).click()

    def view_products(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.PRODUCTS)).click()

    def add_product(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.ADD_PRODUCT)).click()

    def input_product_name(self, product_name):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.INPUT_PRODUCT_NAME)
                                            ).send_keys(product_name)

    def input_meta_tag_title(self, tag_title):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.INPUT_PRODUCT_META_TAG_TITLE)
                                            ).send_keys(tag_title)

    def switch_to_data_in_product_profile(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.DATA_BTN_IN_PRODUCT_PROFILE)
                                            ).click()

    def input_model(self, model):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.MODEL)
                                            ).send_keys(model)

    def save_product(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.SAVE_PRODUCT)
                                            ).click()

    def get_success_alert(self):
        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(
            locators.ALERT_ABOUT_SUCCESS_SAVE_PRODUCT)).text

    def filter_by_product_name(self, product_name):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.FILTER_BY_PRODUCT_NAME)
                                            ).send_keys(product_name)

    def filter_products(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.FILTER_BTN)
                                            ).click()

# RecursionError ??
#    def filter_products_by_product_name(self, product_name):
#        self.filter_products_by_product_name(product_name)
#        self.filter_products()

    def get_model_name(self):
        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.MODEL_NAME_AFTER_FILTRATION)).text

    def check_warning_message(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locators.WARNING_MSG))

    def find_forgotten_password_btn(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.FORGOTTEN_LOGIN_BTN))

    def select_all_products(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.SELECT_ALL_PRODUCTS)).click()

    def select_first_product(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.SELECT_FIRST_PRODUCT)).click()

    def delete_products(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.DELETE_BTN)).click()

    def get_products_list(self):
        return WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.TABLE_BODY)).text

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.submit_login()

    def view_customers(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.CUSTOMERS)).click()

    def filter_by_fullname(self, fullname):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.FILTER_BY_CUSTOMER_FULL_NAME)
                                            ).send_keys(fullname)
        self.filter_products()

    def fullname_in_first_entry(self):
        return WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(
            locators.TABLE_COLUMN_FULLNAME)).text

    def select_all_customers(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.SELECT_ALL_CUSTOMERS)).click()

