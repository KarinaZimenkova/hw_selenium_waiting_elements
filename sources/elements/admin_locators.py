from selenium.webdriver.common.by import By


class AdminPageLocators:
    USERNAME = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BTN = "[type='submit']"
    # Предупреждение при попытке залогиниться с пустыми кредами
    WARNING_MSG = (By.CSS_SELECTOR, "#content > div > div > div > div > div.panel-body > div > i")
    FORGOTTEN_LOGIN_BTN = (By.CSS_SELECTOR,
                           "#content > div > div > div > div > div.panel-body > form > div:nth-child(2) > span > a")
