from .base_page import BasePage
from .locator import LoginPageLocators, BasePageLocators
import time, faker


class LoginPage(BasePage, LoginPageLocators):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'This is not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*self.LOGIN_BUTTON), 'There is no button login'

    def should_be_register_form(self):
        assert self.is_element_present(*self.REGISTER_BUTTON), 'There is no button registration'

    def register_new_user(self, email, password):
        link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        page = BasePage(self.browser, link)
        self.open()
        page.browser.find_element(*LoginPageLocators.EMAIL_LOC).send_keys(email)
        page.browser.find_element(*LoginPageLocators.PASSWORD_LOC).send_keys(password)
        page.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_LOC).send_keys(password)
        page.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
        page.should_be_authorized_user()

    def generation_email(self):
        email = str(time.time()) + '@fakemail.org'
        return email

    def generation_password(self):
        fake_password = faker.Faker()
        password = fake_password.password()
        return password


