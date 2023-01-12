from selenium.webdriver.common.by import By


class MainPageLocators:

    VIEW_SHOPPING_CART_BTN = (By.CSS_SELECTOR, "button.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle")
    TEXT_IN_SHOPPING_CART = (By.CSS_SELECTOR, "p.text-center")
    TOTAL_WISH_LIST = (By.CSS_SELECTOR, "a#wishlist-total")
    SEARCH_BLOCK = (By.CSS_SELECTOR, "#search")
