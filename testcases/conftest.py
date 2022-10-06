import pytest
from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver as selenium_webdriver

@pytest.fixture()
def web_setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = selenium_webdriver.Chrome(options=chrome_options)
        driver.implicitly_wait(3)
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        driver = webdriver.Chrome() # if not pass any browser name in cmd then run in chrome default browser, webdriver.Ie()
        driver.maximize_window()
    return driver

def pytest_addoption(parser): # This will get the value from CLI/Hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to web_setup method
    return request.config.getoption("--browser")

# pytest HTML report #

# It is hook for Adding Environment info to  HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name']  = 'Customers'
    config._metadata['Tester Name']  = 'Hemin'

# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
