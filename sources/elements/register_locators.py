from selenium.webdriver.common.by import By


class RegisterPageLocators:
    HEADER = (By.CSS_SELECTOR, "#content > h1")
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    EMAIL = (By.CSS_SELECTOR, "#input-email")
    MSISDN = (By.CSS_SELECTOR, "#input-telephone")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#input-confirm")
    ACCEPTANCE_OF_NEWSLETTER = (By.CSS_SELECTOR,
                                "#content > form > fieldset:nth-child(3) > div > div > label:nth-child(2) "
                                "> input[type=radio]")
    PRIVACY_POLICY = (By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#content > form > div > div > input.btn.btn-primary")
    SUCCESS_REGISTRATION_HEADER = (By.CSS_SELECTOR, "#content > h1")
    CONTINUE_BTN_AFTER_SUCCESS_REGISTRATION = (By.CSS_SELECTOR, "#content > div > div > a")
    EDIT_ACCOUNT = (By.CSS_SELECTOR, "#column-right > div > a:nth-child(2)")
