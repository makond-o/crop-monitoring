from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self._login_tab = (By.CSS_SELECTOR, 'button[data-id="sign-in-button"]')
        self._email_field = (By.CSS_SELECTOR, 'input[data-id="email"]')
        self._password_field = (By.CSS_SELECTOR, 'input[data-id="password"]')
        self._sign_in_button = (By.CSS_SELECTOR, 'button[data-id="sign-in-btn"]')

    def set_email(self, value: str):
        self.enter_text(self._email_field, value)

    def set_password(self, value: str):
        self.enter_text(self._password_field, value)

    def click_sign_in_button(self):
        self.click(self._sign_in_button)

    def click_sign_in_tab(self):
        self.click(self._login_tab)

    def login(self, email: str, password: str):
        if not self.is_login_tab_checked():
            self.click_sign_in_tab()
        self.set_email(email)
        self.set_password(password)
        self.click_sign_in_button()

    def is_login_tab_checked(self):
        attribute_value = self._wait.until(
            expected_conditions.visibility_of_element_located(self._login_tab)).get_attribute('class')
        is_checked = True if attribute_value == 'checked' else False
        return is_checked
