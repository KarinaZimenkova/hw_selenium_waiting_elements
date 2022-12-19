import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FFService
# from selenium.webdriver.opera.service import Service as OperaService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="http://172.19.0.1:8081")
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/Documents/selenium_drivers"))
    parser.addoption("--headless", action="store_true")


@pytest.fixture
def browser(request):
    # Сбор параметров запуска для pytest
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    drivers = request.config.getoption("--drivers")
    headless = request.config.getoption("--headless")

    if browser == "chrome":
        # В selenium 4 рекомендуют использование такого подхода
        options = ChromeOptions()
        options.headless = headless
        service = ChromiumService(executable_path=drivers + "/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "firefox":
        service = FFService(executable_path=drivers + "/geckodriver")
        driver = webdriver.Firefox(service=service)
    else:
        driver = webdriver.Opera(executable_path=drivers + "/operadriver")

    driver.maximize_window()

    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
