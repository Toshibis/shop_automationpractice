from shop_automationpractice.pages.basket_page import BasketPage


def test_successfully_adding_product_to_cart(browser):
    link = "http://automationpractice.com/index.php?id_product=2&controller=product"
    page = BasketPage(browser, link)
    page.open()
    page.add_product_to_basket()
