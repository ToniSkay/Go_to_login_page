from selenium.webdriver.common.by import By

class AddToBasketTest:
    BASKET_SELECT = (By.CSS_SELECTOR, '#add_to_basket_form .btn')

    EXPECTED_NAME_PRODUCT = (By.CSS_SELECTOR, 'div.col-sm-6.product_main h1')
    REAL_NAME_PRODUCT = (By.CSS_SELECTOR, 'div.alertinner strong')

    EXPECTED_PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.col-sm-6.product_main .price_color')
    REAL_PRICE_PRODUCT = (By.CSS_SELECTOR, 'div.alertinner p strong ')

class BasePageLocators:
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators:
    LOGIN_BUTTON = (By.NAME, 'login_submit')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')
    EMAIL_LOC = (By.ID, 'id_registration-email')
    PASSWORD_LOC = (By.ID, 'id_registration-password1')
    REPEAT_PASSWORD_LOC = (By.ID, 'id_registration-password2')
