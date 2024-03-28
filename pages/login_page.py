from selenium.common.exceptions import NoSuchFrameException

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.driver.current_url(), 'url address is incorrect'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        try:
            self.driver.find_element(*LoginPageLocators.LOGIN_EMAIL_INP_FORM)
            self.driver.find_element(*LoginPageLocators.LOGIN_PASSWORD_INP_FORM)
            self.driver.find_element(*LoginPageLocators.LOGIN_BTN)
            flag_login_form = True
        except NoSuchFrameException:
            flag_login_form = False

        assert flag_login_form, 'Login form is not present'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        # реализуйте проверку, что есть форма логина
        try:
            self.driver.find_element(*LoginPageLocators.REGISTRATION_EMAIL_INP_FORM)
            self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1_INP_FORM)
            self.driver.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2_INP_FORM)
            self.driver.find_element(*LoginPageLocators.REGISTRATION_BTN)
            flag_register_form = True
        except NoSuchFrameException:
            flag_register_form = False

        assert flag_register_form, 'Registration form is not present'
