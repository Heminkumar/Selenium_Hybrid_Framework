# Selenium_Hybrid_Framework
This Hybrid Framework is designed for Backend Ecommerce website (https://admin-demo.nopcommerce.com/) and framework is used with below items:
1. Selenium
2. pytest
3. pytest-html
4. pytest-xdist
5. openpyxl
6. allure-pytest

In this pytest FW, logger functionality is changed so refer utilities/customLogger.py for details for Linux platform

Run Command:- 
1) pytest -v -n=3 --html=Reports/report.html testcases/*  --browser chrome
   
2) pytest -v -n=3 --html=Reports/report.html testcases/test_login.py  --browser chrome
3) pytest -v -n=3 --html=Reports/report.html testcases/test_login.py  --browser firefox