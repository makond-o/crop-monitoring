from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 10)

    def is_visible(self, by_locator):
        element = self._wait.until(expected_conditions.visibility_of_element_located(by_locator))
        return bool(element)

    def is_selected(self, by_locator):
        is_selected = self._wait.until(expected_conditions.visibility_of_element_located(by_locator)).is_selected()
        return is_selected

    def click(self, by_locator):
        self._wait.until(expected_conditions.element_to_be_clickable(by_locator)).click()

    def enter_text(self, by_locator, text):
        return self._wait.until(expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = self._wait.until(expected_conditions.visibility_of_element_located(by_locator))
        return element.text
