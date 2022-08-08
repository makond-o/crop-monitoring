import pytest
from config.config import TestData
from pages.confirm_email_page import ConfirmEmailPage
from pages.registration_page import RegistrationPage


@pytest.mark.usefixtures('setup', 'get_unregistered_email')
class TestRegistration:

    def test_registration(self):
        registration_page = RegistrationPage(self.driver)
        confirm_email_page = ConfirmEmailPage(self.driver)
        registration_page.sign_up(
            TestData.USER_FIRST_NAME, TestData.USER_SECOND_NAME, self.valid_email, TestData.PASSWORD)
        assert confirm_email_page.is_confirm_code_field_exist()
        actual_confirmation_email = confirm_email_page.get_confirmation_email()
        assert actual_confirmation_email == self.valid_email
