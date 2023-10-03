import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def click_element(self, selector):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(selector)
        )
        element.click()

    def send_keys_to_element(self, selector, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(selector)
        )
        element.send_keys(text)
