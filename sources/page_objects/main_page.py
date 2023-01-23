from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sources.elements.main_locators import MainPageLocators as locators


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def find_logo(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of(self.driver.find_element_by_id('logo')))

    def view_shopping_cart(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(
                locators.VIEW_SHOPPING_CART_BTN)).click()

    def find_text_in_shopping_cart(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.TEXT_IN_SHOPPING_CART))

    def find_total_wish_list(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.TOTAL_WISH_LIST))

    def find_search_block(self):
        WebDriverWait(self.driver, 1).until(
            EC.visibility_of_element_located(locators.SEARCH_BLOCK))

    def view_list_of_currencies(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(
                locators.CURRENCY_DROPDOWN_BTN)).click()

    def select_eur(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(
                locators.EUR)).click()

    def select_gbp(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(
                locators.GBP)).click()

    def add_product_to_shopping_cart(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(
                locators.ADD_PRODUCT_TO_SHOPPING_CART)).click()

    def get_currency_in_shopping_cart(self):
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(
                locators.CURRENCY_IN_SHOPPING_CART)).text
