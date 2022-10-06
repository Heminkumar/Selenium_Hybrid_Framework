import pytest
from selenium import webdriver
import unittest

@pytest.fixture()
def web_setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        driver = webdriver.Chrome() # if not pass any browser then run in chrome default browser, webdriver.Ie()
        driver.maximize_window()
    return driver

def pytest_addoption(parser): # This will get the value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to web_setup method
    return request.config.getoption("--browser")