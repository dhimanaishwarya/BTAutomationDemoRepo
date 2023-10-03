import pytest

from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utils.baseClass import BaseClass
from utils.testdata.LoginData import login_data


class TestLoginPage(BaseClass):

    @pytest.mark.parametrize("user_data", [login_data["STANDARD_USER"]])
    def test_default_sort(self, user_data):
        login_page = LoginPage(self.driver)
        login_page.perform_login(user_data["username"], user_data["password"])
        home_page = HomePage(self.driver)
        item_names = home_page.get_list_of_item_names()
        for i in range(len(item_names)-1):
            assert item_names[i] <= item_names[i+1], "Products {0} and {1} are not ordered correctly.".format(item_names[i], item_names[i+1])
        print("test_sort_a_to_z finished successfully.")

    @pytest.mark.parametrize("user_data", [login_data["STANDARD_USER"]])
    def test_verify_user_can_change_sort_order(self, user_data):
        login_page = LoginPage(self.driver)
        login_page.perform_login(user_data["username"], user_data["password"])
        home_page = HomePage(self.driver)
        home_page.sort_products_high_to_low()
        product_prices = home_page.get_list_of_product_prices()
        for i in range(len(product_prices) - 1):
            assert product_prices[i] >= product_prices[i + 1], "Products {0} and {1} are not ordered correctly.".format(product_prices[i], product_prices[i + 1])
        print("test_sort_high_to_low finished successfully.")
