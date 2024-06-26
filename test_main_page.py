import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage:

    '''
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.product = ProductFactory(title="Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        self.product.delete()
    '''

    def test_guest_can_go_to_login_page(self, driver):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
        main_page = MainPage(driver, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(driver, driver.current_url)
        login_page.should_be_login_page()
        # login_page = page.go_to_login_page()
        # login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, driver):
        link = 'http://selenium1py.pythonanywhere.com/'
        main_page = MainPage(driver, link)
        main_page.open()
        main_page.go_to_basket_page()
        basket_page = BasketPage(driver, driver.current_url)
        basket_page.should_not_be_product_in_basket()
        basket_page.is_basket_empty_message()
