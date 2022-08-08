import pytest
from config.config import TestData
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures('setup')
class TestLogin:

    def test_login(self):
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)
        login_page.login(TestData.EMAIL, TestData.PASSWORD)
        assert home_page.is_user_menu_button_exist()
        actual_user_name = home_page.get_user_name()
        expected_user_name = TestData.USER_FIRST_NAME + ' ' + TestData.USER_SECOND_NAME
        assert actual_user_name == expected_user_name
        home_page.logout()
