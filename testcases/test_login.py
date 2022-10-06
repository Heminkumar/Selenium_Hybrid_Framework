import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
import time

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserpassword()
    logger = LogGenerator.loggen()

    def test_homePageTitle(self,web_setup):
        #self.driver = webdriver.Chrome() - we created setup as fixtures so comment this line
        self.logger.info("********** Test_001_Login **********")
        self.logger.info("********** Verifying Home Page Title **********")
        self.driver = web_setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Home Page title Test is Passed **********")
        else:
            self.driver.save_screenshot(".//Screenshots//test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home Page title Test is Failed **********")
            assert False

    def test_login(self,web_setup):
        self.logger.info("********** Verifying Login Test **********")
        self.driver = web_setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_login_title = self.driver.title
        if actual_login_title == "Dashboard / nopCommerce administration":
            self.logger.info("********** Login Test is Passed **********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.logger.error("********** Login Test is Failed **********")
            self.driver.close()
            assert False

    def test_logout(self,web_setup):
        self.logger.info("********** Verifying Logout Test **********")
        self.driver = web_setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(3)
        self.lp.clickLogout()
        actual_title = self.driver.title
        if actual_title == "Your store. Login":
            self.logger.info("********** Logout Test is Passed **********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//test_homePageTitle.png")
            self.logger.info("********** Logout Test is Failed **********")
            self.driver.close()
            assert False