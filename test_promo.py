import pytest
from selenium.common.exceptions import NoSuchElementException

from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_id', ['0', '1', '2', '3', '4', '5',
                                      pytest.param('6', marks=pytest.mark.xfail),
                                      '7', '8', '9'])
def test_add_to_basket_from_product_page(driver, promo_id):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_id}'
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
