from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.baseClass import BaseClass


class HomePage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.inventory_item_name_selector = (By.CLASS_NAME, "inventory_item_name")
        self.inventory_item_element = (By.CLASS_NAME, "inventory_item")
        self.inventory_item_price_selector = (By.CLASS_NAME, "inventory_item_price")
        self.sort_high_to_low_selector = (
            By.CSS_SELECTOR,
            "#header_container > div.header_secondary_container > div > span > select > option:nth-child(4)"
        )
        self.sort_menu_selector = (
            By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select'
        )
        self.ADD_TO_CART_BUTTON_XPATH = ".//div[3]/button"
        self.hamburger_menu_element = (
            By.ID, "react-burger-menu-btn"
        )
        self.logout_element = (By.ID, "logout_sidebar_link")
        self.cart_selector = (By.CLASS_NAME, "shopping_cart_link")

    def get_list_of_item_names(self):
        products = self.driver.find_elements(*self.inventory_item_name_selector)
        return [item.text for item in products]

    def get_list_of_product_prices(self):
        products = self.driver.find_elements(*self.inventory_item_price_selector)
        return [float(item.text.replace("$", "")) for item in products]

    def click_product_sort_menu(self):
        self.click_element(self.sort_menu_selector)

    def sort_products_high_to_low(self):
        self.click_product_sort_menu()
        sort_option = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.sort_high_to_low_selector)
        )
        sort_option.click()

    def get_all_product_elements(self):
        products = self.driver.find_elements(*self.inventory_item_element)
        return products

    def add_three_products_to_cart(self):
        product_elements = self.get_all_product_elements()
        for i, product in enumerate(product_elements):
            if i >= 3:
                break

        add_cart_buttons = product.find_elements(By.XPATH, self.ADD_TO_CART_BUTTON_XPATH)
        for button in add_cart_buttons:
            button.click()

    def click_logout(self):
        element = self.driver.find_element(By.ID, self.logout_element)
        self.click_element(element)

    def click_cart(self):
        self.click_element(self.cart_selector)

    def click_hamburger_menu(self):
        element = self.driver.find_element(By.ID, self.hamburger_menu_element)
        self.click_element(element)
