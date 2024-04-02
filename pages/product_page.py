import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        btn_add_to_basket = self.driver.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        btn_add_to_basket.click()

    def get_name_and_price_of_product(self):
        product_name = self.driver.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        product_price = self.driver.find_element(*ProductPageLocators.PRICE_OF_PRODUCT).text
        return product_name, product_price

    def get_name_and_price_of_product_added_to_basket(self):
        product_name_added_to_basket = self.driver.find_element(
            *ProductPageLocators.NAME_OF_PRODUCT_ADDED_TO_BASKET).text
        product_price_added_to_basket = self.driver.find_element(
            *ProductPageLocators.PRICE_OF_PRODUCT_ADDED_TO_BASKET).text
        return product_name_added_to_basket, product_price_added_to_basket

    def guest_didnt_see_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.NAME_OF_PRODUCT_ADDED_TO_BASKET), \
            'There are success message'

    def success_message_disappeared(self):
        assert self.is_disappeared(ProductPageLocators.NAME_OF_PRODUCT_ADDED_TO_BASKET), \
            'Success message didn\t disappeared'




