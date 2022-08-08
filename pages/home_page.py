from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver: Chrome):
        super().__init__(driver)
        self._user_menu_button = (By.CSS_SELECTOR, 'button[name=user-menu]')
        self._user_name = (By.CSS_SELECTOR, '*[class=full-user-name]')
        self._logout_button = (By.CSS_SELECTOR, 'button[data-id="log-out-button"]')

    def is_user_menu_button_exist(self):
        is_visible = self.is_visible(self._user_menu_button)
        return is_visible

    def get_user_name(self):
        user_name = self.get_element_text(self._user_name)
        return user_name

    def logout(self):
        if expected_conditions.invisibility_of_element_located(self._logout_button):
            self.click(self._user_menu_button)
        self.click(self._logout_button)
        self._wait.until(expected_conditions.invisibility_of_element_located(self._user_menu_button))
