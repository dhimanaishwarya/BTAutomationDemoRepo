import pytest

from pageObjects.LoginPage import LoginPage
from utils.baseClass import BaseClass
from utils.testdata.LoginData import login_data


class TestLoginPage(BaseClass):

    @pytest.mark.parametrize("user_data", [login_data["STANDARD_USER"], login_data["PERFORMANCE_GLITCH_USER"]])
    def test_login_valid_user(self, user_data):
        login_page = LoginPage(self.driver)
        login_page.enter_username(user_data["username"])
        login_page.enter_password(user_data["password"])
        login_page.click_login()
        assert not login_page.error_message_exists()

    @pytest.mark.parametrize("user_data", [login_data["LOCKED_OUT_USER"]])
    def test_login_locked_out_user(self, user_data):
        login_page = LoginPage(self.driver)
        login_page.perform_login(user_data["username"], user_data["password"])
        assert login_page.error_message_exists()
        print(login_page.get_error_message_text())
        print("test_login_locked_out_user finished successfully.")
