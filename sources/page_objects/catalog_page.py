from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sources.elements.catalog_locators import CatalogPageLocators as locators


class CatalogPage:
    path = "/desktops"

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url + self.path)

    def find_desktop_title(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.DESKTOP_TITLE))

    def find_product_image(self, url):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, locators.PRODUCT_IMG_CSS_SELECTOR.replace("http://{host}:{port}", url))))

    def switch_to_list_view(self):
        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.LIST_VIEW_BTN)).click()

    def add_to_wish_list(self):
        WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located(locators.ADD_TO_WISH_LIST_BTN)).click()

    def check_alert_for_unauthorized_user(self):
        """Проверка алерта для неавторизованного пользователя при добавлении товара в список избранных"""

        WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locators.ALERT_FOR_UNAUTHORIZED_USER))
