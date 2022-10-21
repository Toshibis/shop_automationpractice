from pages.base_page import BasePage
from .locators import ShopLocators
import time


class MainPage(BasePage):
    def should_be_search_product(self):
        search = self.browser.find_element(*ShopLocators.SEARCH_FIELD)
        search.send_keys("Faded Short Sleeve T-shirts")
        button = self.browser.find_element(*ShopLocators.SEARCH_BTN)
        button.click()
        time.sleep(4)
        assert self.is_element_present(*ShopLocators.SEARCH_RESULT), \
            "T-shirts page was not open"

    def should_be_popular_list_as_default(self):
        default_element = self.browser.find_element(*ShopLocators.POPULAR_LIST)
        default_text = default_element.text
        assert "POPULAR" == default_text, \
            "Popular list not default"

    def should_be_discount_products_in_bestsellers_list(self):
        bestsellers_list = self.browser.find_element(*ShopLocators.BESTSELLERS_LIST)
        bestsellers_list.click()
        assert self.is_element_present(*ShopLocators.BESTSELLERS_ITEM), \
            "Discount_products are absent"
