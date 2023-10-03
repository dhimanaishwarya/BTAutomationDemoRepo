from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expected_conditions
from utils.baseClass import BaseClass


class CartPage(BaseClass):

    def __init__(self, driver):
        self.continue_shopping_button_element = (By.CLASS_NAME, "btn_secondary")
        self.checkout_button_element = (By.CLASS_NAME, "checkout_button")
        self.item_price_element = (By.CLASS_NAME, "inventory_item_price")
        self.remove_button_element = (By.CLASS_NAME, "cart_button")
        self.subheader_element = (By.CLASS_NAME, 'subheader')

    def click_continue_shopping_button(self):
        self.click_element(self.continue_shopping_button_element)

    def click_checkout_button(self):
        self.click_element(self.checkout_button_element)

    def remove_all_from_cart(self):
        remove_buttons = self.driver.find_elements(*self.remove_button_element)
        while remove_buttons:
            remove = self.driver.find_element(*self.remove_button_element)
            remove.click()
            remove_buttons = self.driver.find_elements(*self.remove_button_element)

    def get_subheader(self):
        element = self.driver.find_element(*self.subheader_element)
        return element.text

    def get_sum_of_prices(self):
        price_elements = self.driver.find_elements(*self.item_price_element)
        total = 0.0
        for price in price_elements:
            total += float(price.text)
        return total
