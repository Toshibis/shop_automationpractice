from shop_automationpractice.pages.main_page import MainPage


def test_searching_products(browser):
    link = "http://automationpractice.com/index.php"
    page = MainPage(browser, link)
    page.open()
    page.should_be_search_product()


def test_popular_list_as_default(browser):
    link = "http://automationpractice.com/index.php"
    page = MainPage(browser, link)
    page.open()
    page.should_be_popular_list_as_default()


def test_discount_products_in_bestsellers_list(browser):
    link = "http://automationpractice.com/index.php"
    page = MainPage(browser, link)
    page.open()
    page.should_be_discount_products_in_bestsellers_list()