from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = By.CSS_SELECTOR, '#login_link'
    LOGIN_LINK_INVALID = By.CSS_SELECTOR, '#login_link_invalid'


class LoginPageLocators:
    LOGIN_EMAIL_INP_FORM = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD_INP_FORM = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_FORGOT_PASSWORD_BTN = (By.CSS_SELECTOR, 'form a')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTRATION_EMAIL_INP_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_1_INP_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_2_INP_FORM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_BASKET_BTN = By.CSS_SELECTOR, '#add_to_basket_form button'
    PRICE_OF_PRODUCT = By.CSS_SELECTOR, '.price_color'
    NAME_OF_PRODUCT = By.CSS_SELECTOR, '.product_main h1'
    NAME_OF_PRODUCT_ADDED_TO_BASKET = By.CSS_SELECTOR, '#messages div.alert:nth-child(1) strong'
    PRICE_OF_PRODUCT_ADDED_TO_BASKET = By.CSS_SELECTOR, '#messages div.alert:nth-child(3) strong'

