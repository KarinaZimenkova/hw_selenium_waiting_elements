from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sources.elements.card_locators import CardPageLocators as locators


class CardPage:
    path = "/desktops/canon-eos-5d"

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + self.path)

    def expand_list_of_colors(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.LIST_OF_COLORS)).click()

    def choose_red_color(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.RED_COLOR)).click()

    def add_product_to_shopping_cart(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.ADD_TO_SHOPPING_CART_BTN)).click()

    def expand_shopping_cart(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.EXPAND_SHOPPING_CART_BTN)).click()

    def remove_product_from_shopping_cart(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(
            locators.REMOVE_PRODUCT_FROM_SHOPPING_CART_BTN)).click()
