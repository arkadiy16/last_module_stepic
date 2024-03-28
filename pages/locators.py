from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_EMAIL_INP_FORM = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWORD_INP_FORM = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button[name="login_submit"]')

    REGISTRATION_EMAIL_INP_FORM = (By.CSS_SELECTOR, '#id_registraion-email')
    REGISTRATION_PASSWORD_1_INP_FORM = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD_2_INP_FORM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BTN = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
