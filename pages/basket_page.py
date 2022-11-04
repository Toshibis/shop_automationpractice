from .base_page import BasePage
from .data import AuthorisationData
from .locators import BasketPageLocators, LoginPageLocators
from .locators import CheckOutLocators
from .locators import MainPageLocators
import time


class BasketPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*BasketPageLocators.PRODUCT_COLOR).click()
        self.browser.find_element(*BasketPageLocators.ADD_TO_CART_BTN).click()
        time.sleep(3)
        assert "Product successfully added to your shopping cart" == self.browser.find_element(*BasketPageLocators.SUCCESSFULLY_ADDING_TO_CART).text, \
            "Product was not add to cart"

    def check_out(self):
        self.browser.find_element(*BasketPageLocators.PRODUCT_COLOR).click()
        self.browser.find_element(*BasketPageLocators.ADD_TO_CART_BTN).click()
        self.browser.find_element(*BasketPageLocators.CHECKOUT_BTN).click()
        self.browser.find_element(*CheckOutLocators.PROCEED_TO_CHECKOUT_BTN_STEP1).click()
        self.browser.find_element(*LoginPageLocators.SIGNIN_EMAIL_FIELD).send_keys(*AuthorisationData.USER_EMAIL_TOTO)
        self.browser.find_element(*LoginPageLocators.SIGNIN_PASSWORD_FIELD).send_keys(*AuthorisationData.USER_PASS_TOTO)
        self.browser.find_element(*CheckOutLocators.PROCEED_TO_CHECKOUT_SIGN_IN_BTN).click()
        self.browser.find_element(*CheckOutLocators.PROCEED_TO_CHECKOUT_BTN_STEP3).click()
        self.browser.find_element(*CheckOutLocators.AGREE_BTN).click()
        self.browser.find_element(*CheckOutLocators.PROCEED_TO_CHECKOUT_BTN_STEP4).click()
        self.browser.find_element(*CheckOutLocators.PAY_BACK).click()
        self.browser.find_element(*CheckOutLocators.CONFIRM_ORDER).click()
        assert self.is_element_present(*CheckOutLocators.SUCCESSFULLY_ORDER_MESSAGE), \
            "Checkout was not successfully"
