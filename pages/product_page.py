from .base_page import BasePage
from .locator import AddToBasketTest
import time

class PageObject(BasePage, AddToBasketTest):
    def expected_product_name_and_price(self):
        self.expected_name = self.browser.find_element(*AddToBasketTest.EXPECTED_NAME_PRODUCT).text
        self.expected_price = self.browser.find_element(*AddToBasketTest.EXPECTED_PRICE_PRODUCT).text

    def add_to_basket(self):
        self.browser.execute_script('window.scrollTo(0,100)')
        self.browser.find_element(*AddToBasketTest.BASKET_SELECT).click()

    def check_correct_product_name(self):
        real_name = self.browser.find_element(*AddToBasketTest.REAL_NAME_PRODUCT).text
        assert self.expected_name == real_name, 'Invalid product name in basket'

    def check_correct_product_price(self):
        real_price = self.browser.find_element(*AddToBasketTest.REAL_PRICE_PRODUCT).text
        assert self.expected_price == real_price, 'Invalid product price in basket'

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
        pages_checking = BasePage(self.browser, link)
        pages_checking.open()
        self.browser.find_element(*AddToBasketTest.BASKET_SELECT).click()
        assert self.is_not_element_present(*AddToBasketTest.REAL_NAME_PRODUCT), '1 test False'

    def test_guest_cant_see_success_message(self):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
        pages_checking = BasePage(self.browser, link)
        pages_checking.open()
        assert self.is_not_element_present(*AddToBasketTest.REAL_NAME_PRODUCT), '2 test False'

    def test_message_disappeared_after_adding_product_to_basket(self):
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
        pages_checking = BasePage(self.browser, link)
        pages_checking.open()
        self.browser.find_element(*AddToBasketTest.BASKET_SELECT).click()
        time.sleep(1)
        assert self.is_disappeared(*AddToBasketTest.REAL_NAME_PRODUCT), '3 test False'

    def test_guest_should_see_login_link_on_product_page(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasePage(self.browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = BasePage(self.browser, link)
        page.open()
        page.go_to_login_page()




