class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'

class LoginPageLocators:
    LOGIN_BUTTON = (By.NAME, 'login_submit')
    REGISTER_BUTTON = (By.NAME, 'registration_submit') #добавить в файл locator.py

    def should_not_be_success(self):
        assert self.is_not_element_present(*AddToBasketTest.REAL_NAME_PRODUCT), 'Real name wrong'