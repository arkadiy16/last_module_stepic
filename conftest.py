import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: by short name")


@pytest.fixture(scope="function")
def driver(request):
    language_name = request.config.getoption("language")
    options = Options()

    options.add_experimental_option('prefs', {'intl.accept_languages': f'{language_name}'})

    driver = webdriver.Chrome(options)

    yield driver
    print("\nquit browser..")
    driver.quit()
