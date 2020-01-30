from .base_page import BasePage
from .locator import LoginPageLocators


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
