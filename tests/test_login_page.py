from shop_automationpractice.pages.login_page import LoginPage


def test_registration_user(browser):
    link = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    page = LoginPage(browser, link)
    page.open()
    page.sign_up_new_user()


def test_sign_in_user(browser):
    link = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    page = LoginPage(browser, link)
    page.open()
    page.sign_in_user()
