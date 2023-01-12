from selenium.webdriver.common.by import By


class AdminPageLocators:
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BTN = "[type='submit']"
    # Предупреждение при попытке залогиниться с пустыми кредами
    WARNING_MSG = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > div > i")
    FORGOTTEN_LOGIN_BTN = (By.CSS_SELECTOR,
                           "#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a")
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    PRODUCTS = (By.CSS_SELECTOR, "#collapse1 > li:nth-child(2) > a")
    ADD_PRODUCT = (By.CSS_SELECTOR, "#content > div.page-header > div > div > a")
    INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name1")
    INPUT_PRODUCT_META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title1")
    DATA_BTN_IN_PRODUCT_PROFILE = (By.CSS_SELECTOR, "#form-product > ul > li:nth-child(2)")
    MODEL = (By.CSS_SELECTOR, "#input-model")
    SAVE_PRODUCT = (By.CSS_SELECTOR, "#content > div.page-header > div > div > button > i")
    ALERT_ABOUT_SUCCESS_SAVE_PRODUCT = (By.CSS_SELECTOR,
                                        "#content > div.container-fluid > div.alert.alert-success.alert-dismissible")
    FILTER_BY_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name")
    FILTER_BTN = (By.CSS_SELECTOR, "#button-filter")
    MODEL_NAME_AFTER_FILTRATION = (By.CSS_SELECTOR, "#form-product > div > table > tbody > tr > td:nth-child(3)")
