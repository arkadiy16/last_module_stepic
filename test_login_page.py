from .pages.login_page import LoginPage


def test_guest_can_see_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page = LoginPage(driver, link)
    page.open()
    page.should_be_login_page()
