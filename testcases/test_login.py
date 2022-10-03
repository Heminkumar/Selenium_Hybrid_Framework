import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

#@pytest.mark.usefixtures("web_setup")
class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self,web_setup):
        #self.driver = webdriver.Chrome() - we created setup as fixtures so comment this line
        self.driver = web_setup
        self.driver.get(self.baseURL)
        print("self.driver:- ",self.driver)
        actual_title = self.driver.title
        #self.driver.close()
        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".//Screenshots//test_homePageTitle.png")
            self.driver.close()
            assert False

    def test_login(self,web_setup):
        self.driver = web_setup
        self.driver.get(self.baseURL)
        print("self.driver:- ", self.driver)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_login_title = self.driver.title
        #self.driver.close()
        if actual_login_title == "Dashboard / nopCommerce administration":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_login.png")
            self.driver.close()
            assert False