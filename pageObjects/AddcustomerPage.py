# This the class for Customer Page class and we define all locators and action methods under class
import time
from selenium.webdriver.support.ui import Select

<<<<<<< HEAD
class AddCustomer:
    lnkCustomers_menu_xpath = '//a[@href="#"]//p[contains(text(),"Customers")]'
    lnkCustomers_menuItem_xpath = ''
    btnAddNew_xpath = ''
    txtEmail_xpath = ''
    txtPassword_xpath = ''
    txtCustomerRoles_xpath = ''
    lstItemAdministrators_xpath = ''
    lstItemRegistered_xpath = ''
    lstItemGuests_xpath = ''
    lstItemVendors_xpath = ''
    drPmGrOfVendor_xpath = ''
    rdMaleGender_id = ''
    rdFeMaleGender_id = ''
    txtFirstName_xpath = ''
    txtLastName_xpath = ''
    txtDob_xpath = ''
    txtCompanyName_xpath = ''
    txtAdminContent_xpath = ''
    btnSave_xpath = ''

    def __init__(self,driver):
        self.driver = driver
=======
class AddCustomer():
    lnkCustomers_menu_xpath = '//a[@href="#"]//p[contains(text(),"Customers")]'
    lnkCustomers_menuitem_xpath =
    btnAddnew_xpath =
    txtEmail_xpath =
    txtPassword_xpath =
    txtcustomerRoles_xpath =
    lstitemAdministrators_xpath =
    lstitemRegistered_xpath =
    lstitemGuests_xpath =
    lstitemVendors_xpath =
    drpmgrOfVendor_xpath =
    rdMaleGender_id =
    rdFeMaleGender_id =
    txtFirstName_xpath =
    txtLastName_xpath =
    txtDob_xpath =
    txtCompanyName_xpath =
    txtAdminContent_xpath =
    btnSave_xpath =

    def __init__(self,driver):
        self.driver = driver
>>>>>>> origin/master
