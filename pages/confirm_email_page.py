from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ConfirmEmailPage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self._confirm_code_field = (By.CSS_SELECTOR, 'input[data-id="confirm-code-input"]')
        self._email = (By.CSS_SELECTOR, 'div[class="email"]')

    def is_confirm_code_field_exist(self):
        is_visible = self.is_visible(self._confirm_code_field)
        return is_visible

    def get_confirmation_email(self):
        confirmation_email = self.get_element_text(self._email)
        return confirmation_email
