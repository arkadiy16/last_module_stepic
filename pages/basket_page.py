from selenium.common.exceptions import NoSuchElementException

from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty_message(self):
        message = self.driver.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text
        assert 'Your basket is empty.' in message, 'There is product in message'

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(BasketPageLocators.BASKET_SUMMARY), 'There are product in basket'

