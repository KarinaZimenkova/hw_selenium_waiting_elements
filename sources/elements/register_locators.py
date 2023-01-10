from selenium.webdriver.common.by import By


class RegisterPageLocators:
    HEADER = (By.CSS_SELECTOR, "#content > h1")
    FIRSTNAME = (By.CSS_SELECTOR, "#input-firstname")
    LASTNAME = (By.CSS_SELECTOR, "#input-lastname")
    ACCEPTANCE_OF_NEWSLETTER = (By.CSS_SELECTOR,
                                "#content > form > fieldset:nth-child(3) > div > div > label:nth-child(2) "
                                "> input[type=radio]")
    PRIVACY_POLICY = (By.CSS_SELECTOR, "#content > form > div > div > input[type=checkbox]:nth-child(2)")