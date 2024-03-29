import time

from selenium.common.exceptions import NoSuchElementException

from .pages.product_page import ProductPage



def test_add_to_basket_from_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(driver, link)
    page.open()
    product_data = page.get_name_and_price_of_product()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    try:
        product_added_to_basket_data = page.get_name_and_price_of_product_added_to_basket()
    except NoSuchElementException:
        raise NoSuchElementException('Can\'t find message box after added product to basket')
    assert product_data == product_added_to_basket_data, 'To basket added wrong product'
