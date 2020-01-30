from .pages.locator import MainPageLocators
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

def test_can_go_to_login_page(browser):
    link = MainPageLocators.LINK
    login_page = LoginPage(browser, link)
    page = MainPage(browser, link)
    page.open() #открываем браузер с ссылкой указанной в константе
    page.go_to_link_page() #переходим на страницу логина
    login_page.should_be_login_page()
