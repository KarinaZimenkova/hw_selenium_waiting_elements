from selenium.webdriver.common.by import By


class MainPageLocators:

    VIEW_SHOPPING_CART_BTN = (By.CSS_SELECTOR, "button.btn.btn-inverse.btn-block.btn-lg.dropdown-toggle")
    TEXT_IN_SHOPPING_CART = (By.CSS_SELECTOR, "p.text-center")
    TOTAL_WISH_LIST = (By.CSS_SELECTOR, "a#wishlist-total")
    SEARCH_BLOCK = (By.CSS_SELECTOR, "#search")
    CURRENCY_DROPDOWN_BTN = (By.CSS_SELECTOR, "#form-currency > div > button")
    EUR = (By.CSS_SELECTOR, "#form-currency > div > ul > li:nth-child(1) > button")
    GBP = (By.CSS_SELECTOR, "ul > li:nth-child(2) > button")
    CURRENCY_IN_SHOPPING_CART = (By.CSS_SELECTOR, "#cart-total")
    ADD_PRODUCT_TO_SHOPPING_CART = (
        By.CSS_SELECTOR,
        "#content > div.row > div:nth-child(1) > div > div.button-group > button:nth-child(1)")
