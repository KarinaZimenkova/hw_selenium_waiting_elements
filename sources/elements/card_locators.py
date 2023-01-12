from selenium.webdriver.common.by import By


class CardPageLocators:
    LIST_OF_COLORS = (By.CSS_SELECTOR, "#input-option226")
    RED_COLOR = (By.CSS_SELECTOR, "#input-option226 > option:nth-child(2)")
    ADD_TO_SHOPPING_CART_BTN = (By.CSS_SELECTOR, "#button-cart")
    EXPAND_SHOPPING_CART_BTN = (By.CSS_SELECTOR, "#cart")
    REMOVE_PRODUCT_FROM_SHOPPING_CART_BTN = \
        (By.CSS_SELECTOR, "#cart > ul > li:nth-child(1) > table > tbody > tr > td:nth-child(5) > button")
