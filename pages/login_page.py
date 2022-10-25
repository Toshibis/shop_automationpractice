from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def sign_up_new_user(self):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email = str(time.time()) + "@fakeemail.org"
        email_field.send_keys(email)
        button = self.browser.find_element(*LoginPageLocators.CREATE_ACC_BTN)
        button.click()
        assert self.is_element_present(*LoginPageLocators.RESULT), \
            "Form was not open"

