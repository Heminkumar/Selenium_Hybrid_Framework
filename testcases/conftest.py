import pytest
from selenium import webdriver
import unittest

@pytest.fixture()
def web_setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver