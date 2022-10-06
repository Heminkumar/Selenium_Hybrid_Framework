import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGenerator
from utilities import XLUtils
import time

class Test_002_ddt_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = './/TestData/LoginData.xlsx'

    logger = LogGenerator.loggen()

    def test_login_ddt(self,web_setup):
        self.logger.info("********** Test_002_DDT_Login **********")
        self.logger.info("********** Verifying Login DDT Test **********")
        self.driver = web_setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        lst_status = [] # Empty list variable for mark TC as pass/Fail

        for r in range(2,self.rows+1):
            self.username = XLUtils.readData(self.path,'Sheet1',r,1) # give first record
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path, 'Sheet1',r,3)
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            actual_login_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if actual_login_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** Passed ****")
                    time.sleep(7)
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                   # self.driver.close()
                    assert True
                elif self.exp == 'Fail':
                    self.logger.info("**** Failed ****")
                    self.lp.clickLogout()
                    lst_status.append("Fail")

            elif actual_login_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info("**** Failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** Passed ****")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***** Login DDT Test Passed *****")
            self.driver.close()
            assert True
        else:
            self.logger.info("***** Login DDT Test Failed *****")
            self.driver.close()
            assert False

        self.logger.info("****** End of Login DDT Test ******")
        self.logger.info("********** Completed TC Test_002_ddt_Login **********")