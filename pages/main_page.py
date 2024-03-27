import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

from .base_page import BasePage


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.driver.find_element(By.CSS_SELECTOR, '#login_link')
        login_link.click()

    def should_be_login_link(self):
        self.driver.find_element(By.CSS_SELECTOR, '#login_link')
        assert self.is_element_present(By.CSS_SELECTOR, '#login_link_invalid'), \
            'Login link is not present or selector is invalid'
