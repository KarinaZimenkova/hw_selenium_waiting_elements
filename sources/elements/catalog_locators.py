from selenium.webdriver.common.by import By


class CatalogPageLocators:
    DESKTOP_TITLE = (By.CSS_SELECTOR, "[title=Desktops]")
    # При переиспользовании необходимо заменить {host}:{port} на конкретные значения
    PRODUCT_IMG_CSS_SELECTOR = "[src='http://{host}:{port}/image/cache/catalog/demo/apple_cinema_30-228x228.jpg']"
    LIST_VIEW_BTN = (By.CSS_SELECTOR, "button#list-view.btn.btn-default")
    ADD_TO_WISH_LIST_BTN = (By.CSS_SELECTOR, "button[data-original-title='Add to Wish List']")
    ALERT_FOR_UNAUTHORIZED_USER = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
