from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from utils.baseClass import BaseClass


class LoginPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver
        self.username_input_box_element = (By.ID, "user-name")
        self.password_input_box_element = (By.ID, "password")
        self.login_button_element = (By.ID, "login-button")
        self.error_message_element = (By.XPATH, '//*[@id="login_button_container"]/div/form')

    def enter_username(self, username):
        self.send_keys_to_element(self.username_input_box_element, username)

    def enter_password(self, password):
        self.send_keys_to_element(self.password_input_box_element, password)

    def click_login(self):
        self.click_element(self.login_button_element)
        WebDriverWait(self.driver, 5).until(expected_conditions.url_changes)

    def error_message_exists(self):
        error_message = self.driver.find_elements(By.XPATH, self.error_message_element[1])
        return len(error_message) > 0

    def get_error_message_text(self):
        if self.error_message_exists():
            return self.driver.find_elements(By.XPATH, self.error_message_element[1])[0].text
        return None

    def perform_login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
