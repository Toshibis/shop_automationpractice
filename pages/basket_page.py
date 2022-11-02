from .base_page import BasePage
from .locators import BasketPageLocators
import time


class BasketPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*BasketPageLocators.PRODUCT_COLOR).click()
        self.browser.find_element(*BasketPageLocators.ADD_TO_CART_BTN)
        time.sleep(3)
        assert "Product successfully added to your shopping cart" == self.browser.find_element(*BasketPageLocators.SUCCESSFULLY_ADDING_TO_CART).text, \
            "Product was not add to cart"
