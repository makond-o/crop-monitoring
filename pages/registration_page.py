import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self._sign_up_tab = (By.CSS_SELECTOR, 'button[data-id="go-signup-btn"]')
        self._first_name_field = (By.CSS_SELECTOR, 'input[data-id="first_name"]')
        self._last_name_field = (By.CSS_SELECTOR, 'input[data-id="last_name"]')
        self._email_field = (By.CSS_SELECTOR, 'input[data-id="email"]')
        self._password_field = (By.CSS_SELECTOR, 'input[data-id="password"]')
        self._sign_up_button = (By.CSS_SELECTOR, 'button[data-id="sign-up-btn"]')
        self.accept_privacy_policy_checkbox = (By.CSS_SELECTOR, '*[class="mat-checkbox-inner-container"]')

    def set_first_name(self, value: str):
        self.enter_text(self._first_name_field, value)

    def set_last_name(self, value: str):
        self.enter_text(self._last_name_field, value)

    def set_email(self, value: str):
        self.enter_text(self._email_field, value)

    def set_password(self, value: str):
        self.enter_text(self._password_field, value)

    def activate_privacy_policy_checkbox(self):
        self.click(self.accept_privacy_policy_checkbox)

    def click_sign_up_button(self):
        self.click(self._sign_up_button)

    def click_sig_up_tab(self):
        self.click(self._sign_up_tab)

    def is_sign_up_tab_checked(self):
        element_class_value = self._wait.until(
            expected_conditions.visibility_of_element_located(self._sign_up_tab)).get_attribute('class')
        is_checked = True if element_class_value == 'checked' else False
        return is_checked

    def sign_up(self, first_name: str, last_name: str, email: str, password: str):
        if not self.is_sign_up_tab_checked():
            self.click_sig_up_tab()
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_password(password)
        if not self.is_selected(self.accept_privacy_policy_checkbox):
            self.activate_privacy_policy_checkbox()
        time.sleep(2)
        self.click_sign_up_button()
