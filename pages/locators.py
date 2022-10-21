from selenium.webdriver.common.by import By


class ShopLocators:
    SEARCH_FIELD = (By.XPATH, "//input[@id='search_query_top']")
    SEARCH_BTN = (By.XPATH, "//button[@name='submit_search']")
    SEARCH_RESULT = (By.XPATH, "//span[@class='lighter']")
    POPULAR_LIST = (By.XPATH, '//*[@id="home-page-tabs"]/li[1]')
    BESTSELLERS_LIST = (By.XPATH, "//a[@class='blockbestsellers']")
    BESTSELLERS_ITEM = (By.CSS_SELECTOR, ".price-percent-reduction")
