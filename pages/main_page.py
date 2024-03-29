import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # alert = self.driver.switch_to_alert
        # alert.accept()
        # return LoginPage(driver=self.driver, url=self.driver.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
            'Login link is not present or selector is invalid'
