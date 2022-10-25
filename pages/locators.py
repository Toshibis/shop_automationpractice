from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.XPATH, "//input[@id='search_query_top']")
    SEARCH_BTN = (By.XPATH, "//button[@name='submit_search']")
    SEARCH_RESULT = (By.XPATH, "//span[@class='lighter']")
    POPULAR_LIST = (By.XPATH, '//*[@id="home-page-tabs"]/li[1]')
    BESTSELLERS_LIST = (By.XPATH, "//a[@class='blockbestsellers']")
    BESTSELLERS_ITEM = (By.CSS_SELECTOR, ".price-percent-reduction")


class LoginPageLocators:
    EMAIL_FIELD = (By.XPATH, "//input[@id='email_create']")
    CREATE_ACC_BTN = (By.XPATH, "//span[normalize-space()='Create an account']")
    RESULT = (By.XPATH, "//h3[normalize-space()='Your personal information']")
    #Registration form "YOUR PERSONAL INFORMATION"
    CREATE_FORM_PERSONAL_MR = (By.XPATH, "//input[@id='id_gender1']")
    CREATE_FORM_PERSONAL_MRS = (By.XPATH, "//input[@id='id_gender2']")
    CREATE_FORM_PERSONAL_FIRST_NAME = (By.XPATH, "//input[@id='customer_firstname']")
    CREATE_FORM_PERSONAL_LAST_NAME = (By.XPATH, "//input[@id='customer_lastname']")
    CREATE_FORM_PERSONAL_PASSWORD = (By.XPATH, "//input[@id='passwd']")
    CREATE_FORM_PERSONAL_DATE_OF_BIRTH_D = (By.XPATH, "//select[@id='days']")
    CREATE_FORM_PERSONAL_DATE_OF_BIRTH_M = (By.XPATH, "//select[@id='months']")
    CREATE_FORM_PERSONAL_DATE_OF_BIRTH_Y = (By.XPATH, "//select[@id='years']")
    CREATE_FORM_PERSONAL_NEWSLETTER = (By.XPATH, "//label[@for='newsletter']")
    CREATE_FORM_PERSONAL_PARTNERS = (By.XPATH, "//label[@for='optin']")
    # Registration form "YOUR ADDRESS"
    CREATE_FORM_ADDRESS_FIRST_NAME = (By.XPATH, "//input[@id='firstname']")
    CREATE_FORM_ADDRESS_LAST_NAME = (By.XPATH, "//input[@id='lastname']")
    CREATE_FORM_ADDRESS_COMPANY = (By.XPATH, "//input[@id='company']")
    CREATE_FORM_ADDRESS_ADDRESS = (By.XPATH, "//input[@id='address1']")
    CREATE_FORM_ADDRESS_ADDRESS_LINE2 = (By.XPATH, "//input[@id='address2']")
    CREATE_FORM_ADDRESS_CITY = (By.XPATH, "//input[@id='city']")
    CREATE_FORM_ADDRESS_STATE = (By.XPATH, "//select[@id='id_state']")
    CREATE_FORM_ADDRESS_ZIP = (By.XPATH, "//input[@id='postcode']")
    CREATE_FORM_ADDRESS_COUNTRY = (By.XPATH, "//select[@id='id_country']")
    CREATE_FORM_ADDRESS_ADD_INFO = (By.XPATH, "//textarea[@id='other']")
    CREATE_FORM_ADDRESS_HOME_PHONE = (By.XPATH, "//input[@id='phone']")
    CREATE_FORM_ADDRESS_MOBILE_PHONE = (By.XPATH, "//input[@id='phone_mobile']")
    CREATE_FORM_ADDRESS_ASSIGN_AN_ADDRESS_ALIAS = (By.XPATH, "//input[@id='alias']")
    REGISTER_BTN = (By.XPATH, "//span[normalize-space()='Register']")

