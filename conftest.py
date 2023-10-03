import time

import pytest
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

from utils.testdata import LoginData

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        # chrome_driver_path = "./drivers/chromedriver"
        # chrome_service = ChromeService(chrome_driver_path)
        driver = webdriver.Chrome()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(LoginData.URL)
    driver.maximize_window()

    request.cls.driver = driver

    yield
    driver.quit()
    time.sleep(5)




