from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LINK = 'http://selenium1py.pythonanywhere.com/'

class LoginPageLocators:
    LOGIN_BUTTON = (By.NAME, 'login_submit')
    REGISTER_BUTTON = (By.NAME, 'registration_submit')