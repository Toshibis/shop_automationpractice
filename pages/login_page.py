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
            "Registration form was not open"
        mr_rb = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_MR)
        mr_rb.click()
        personal_first_name = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_FIRST_NAME)
        personal_first_name.send_keys("Toto")
        personal_last_name = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_LAST_NAME)
        personal_last_name.send_keys("Otto")
        personal_password = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_PASSWORD)
        personal_password.send_keys("12345")
        date_of_birth_day = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_DATE_OF_BIRTH_D)
        date_of_birth_day.click()
        select_date_of_birth_day = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_SELECT_DATE_OF_BIRTH_D)
        select_date_of_birth_day.click()
        date_of_birth_month = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_DATE_OF_BIRTH_M)
        date_of_birth_month.click()
        select_date_of_birth_month = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_SELECT_DATE_OF_BIRTH_M)
        select_date_of_birth_month.click()
        date_of_birth_year = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_DATE_OF_BIRTH_Y)
        date_of_birth_year.click()
        select_date_of_birth_year = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_SELECT_DATE_OF_BIRTH_Y)
        select_date_of_birth_year.click()
        mailing_list = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_NEWSLETTER)
        mailing_list.click()
        partners = self.browser.find_element(*LoginPageLocators.CREATE_FORM_PERSONAL_PARTNERS)
        partners.click()
        address_first_name = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_FIRST_NAME)
        address_first_name.send_keys("Totow")
        address_last_name = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_LAST_NAME)
        address_last_name.send_keys("Ottow")
        address_company = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_COMPANY)
        address_company.send_keys("Rembrandt")
        address_address = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_ADDRESS)
        address_address.send_keys("Sport ave, 77")
        address_address_line2 = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_ADDRESS_LINE2)
        address_address_line2.send_keys("Sport ave, 55")
        address_city = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_CITY)
        address_city.send_keys("Chicago")
        address_state = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_STATE)
        address_state.click()
        address_select_state = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_SELECT_STATE)
        address_select_state.click()
        address_zip = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_ZIP)
        address_zip.send_keys("58000")
        address_country = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_COUNTRY)
        address_country.click()
        address_select_country = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_SELECT_COUNTRY)
        address_select_country.click()
        address_add_info = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_ADD_INFO)
        address_add_info.send_keys("It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.")
        address_home_phone = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_HOME_PHONE)
        address_home_phone.send_keys("+380991234567")
        address_mob_phone = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_MOBILE_PHONE)
        address_mob_phone.send_keys("+380667654321")
        address_alias = self.browser.find_element(*LoginPageLocators.CREATE_FORM_ADDRESS_ASSIGN_AN_ADDRESS_ALIAS)
        address_alias.send_keys("Office")
        registration_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        registration_btn.click()
        assert self.is_element_present(*LoginPageLocators.SUCCESSFUL_REGISTRATION), "Registration was not complete"
        # print(self.is_not_element_present(*LoginPageLocators.ERROR_OF_FORM).text)




        time.sleep(2)
