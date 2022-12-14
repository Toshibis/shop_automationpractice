from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.XPATH, "//input[@id='search_query_top']")
    SEARCH_BTN = (By.XPATH, "//button[@name='submit_search']")
    SEARCH_RESULT = (By.XPATH, "//span[@class='lighter']")
    POPULAR_LIST = (By.XPATH, '//*[@id="home-page-tabs"]/li[1]')
    BESTSELLERS_LIST = (By.XPATH, "//a[@class='blockbestsellers']")
    BESTSELLERS_ITEM = (By.CSS_SELECTOR, ".price-percent-reduction")



class LoginPageLocators:
    #Sign Up elements
    SIGNUP_EMAIL_FIELD = (By.XPATH, "//input[@id='email_create']")
    CREATE_ACC_BTN = (By.XPATH, "//span[normalize-space()='Create an account']")
    RESULT = (By.XPATH, "//h3[normalize-space()='Your personal information']")
    #Registration form "YOUR PERSONAL INFORMATION"
    CREATE_FORM_PERSONAL_MR = (By.XPATH, "//input[@id='id_gender1']")
    CREATE_FORM_PERSONAL_MRS = (By.XPATH, "//input[@id='id_gender2']")
    CREATE_FORM_PERSONAL_FIRST_NAME = (By.XPATH, "//input[@id='customer_firstname']")
    CREATE_FORM_PERSONAL_LAST_NAME = (By.XPATH, "//input[@id='customer_lastname']")
    CREATE_FORM_PERSONAL_PASSWORD = (By.XPATH, "//input[@id='passwd']")
    CREATE_FORM_PERSONAL_DATE_OF_BIRTH_D = (By.XPATH, "//select[@id='days']")
    CREATE_FORM_PERSONAL_SELECT_DATE_OF_BIRTH_D = (By.XPATH, '//*[@id="days"]/option[11]')
    CREATE_FORM_PERSONAL_DATE_OF_BIRTH_M = (By.XPATH, "//select[@id='months']")
    CREATE_FORM_PERSONAL_SELECT_DATE_OF_BIRTH_M = (By.XPATH, '// *[ @ id = "months"] / option[7]')
    CREATE_FORM_PERSONAL_DATE_OF_BIRTH_Y = (By.XPATH, "//select[@id='years']")
    CREATE_FORM_PERSONAL_SELECT_DATE_OF_BIRTH_Y = (By.XPATH, '//*[@id="years"]/option[24]')
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
    CREATE_FORM_ADDRESS_SELECT_STATE = (By.XPATH, '//*[@id="id_state"]/option[6]')
    CREATE_FORM_ADDRESS_ZIP = (By.XPATH, "//input[@id='postcode']")
    CREATE_FORM_ADDRESS_COUNTRY = (By.XPATH, "//select[@id='id_country']")
    CREATE_FORM_ADDRESS_SELECT_COUNTRY = (By.XPATH, '//*[@id="id_country"]/option[2]')
    CREATE_FORM_ADDRESS_ADD_INFO = (By.XPATH, "//textarea[@id='other']")
    CREATE_FORM_ADDRESS_HOME_PHONE = (By.XPATH, "//input[@id='phone']")
    CREATE_FORM_ADDRESS_MOBILE_PHONE = (By.XPATH, "//input[@id='phone_mobile']")
    CREATE_FORM_ADDRESS_ASSIGN_AN_ADDRESS_ALIAS = (By.XPATH, "//input[@id='alias']")
    REGISTER_BTN = (By.XPATH, "//span[normalize-space()='Register']")
    SUCCESSFUL_REGISTRATION = (By.XPATH, "//p[@class='info-account']")
    ERROR_OF_FORM = (By.XPATH, '//*[@id="center_column"]/div/ol/li')
    # Sign In elements
    SIGNIN_EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    SIGNIN_PASSWORD_FIELD = (By.XPATH, "//input[@id='passwd']")
    SIGNIN_BTN = (By.XPATH, "//span[normalize-space()='Sign in']")
    ACCOUNT_PAGE_CHECK = (By.XPATH, "//p[@class='info-account']")


class BasketPageLocators:
    PRODUCT_COLOR = (By.XPATH, "//a[@id='color_8']")
    ADD_TO_CART_BTN = (By.XPATH, '//*[@id="add_to_cart"]/button')
    SUCCESSFULLY_ADDING_TO_CART = (By.XPATH, "//h2[normalize-space()='Product successfully added to your shopping cart']")
    CHECKOUT_BTN = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')


class CheckOutLocators:
    PROCEED_TO_CHECKOUT_BTN_STEP1 = (By.XPATH, "//a[@class='button btn btn-default standard-checkout button-medium']//span[contains(text(),'Proceed to checkout')]")
    PROCEED_TO_CHECKOUT_SIGN_IN_BTN = (By.XPATH, '//*[@id="SubmitLogin"]')
    PROCEED_TO_CHECKOUT_BTN_STEP2 = (By.XPATH, "//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]")
    AGREE_BTN = (By.XPATH, "//input[@id='cgv']")
    PROCEED_TO_CHECKOUT_BTN_STEP3 = (By.XPATH, '//*[@id="center_column"]/form/p/button')
    PROCEED_TO_CHECKOUT_BTN_STEP4 = (By.XPATH, '//*[@id="form"]/p/button')
    PAY_BACK = (By.XPATH, "//a[@title='Pay by check.']//span[contains(text(),'(order processing will be longer)')]")
    CONFIRM_ORDER = (By. XPATH, "//span[normalize-space()='I confirm my order']")
    SUCCESSFULLY_ORDER_MESSAGE = (By.XPATH, "//p[@class='alert alert-success']")

