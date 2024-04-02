import time

import pytest
from selenium.common.exceptions import NoSuchElementException

from .pages.product_page import ProductPage


def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.guest_didnt_see_success_message()


def test_guest_cant_see_success_message(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(driver, link)
    page.open()
    page.guest_didnt_see_success_message()


def test_message_disappeared_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(driver, link)
    page.open()
    page.add_to_basket()
    page.success_message_disappeared()


