import time
from selenium.webdriver.common.by import By
import pytest
from utilities.customLogger import  LogGen
from utilities.readProperties import ReadConfig
from pageobjects.LoginPage import LoginPage
from utilities import XLUtils
class Test_002_DDT_Login:
    url=ReadConfig.getApplicationURL()
    path=".//testdata/data.xlsx"


    logger=LogGen.loggen()
    def test_login_ddt(self,setup):
        self.driver=setup
        self.logger.info("Test_002_DDT_Login.test_login")
        self.logger.info("Verifying the Login Page")
        time.sleep(2)
        self.driver.get(self.url)
        self.lp=LoginPage(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in a Excel:",self.rows)
        lst_status=[]#empty list variable

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp=XLUtils.readData(self.path,'Sheet1',r,3)
            self.lp.click_home_signin()
            self.lp.set_email(self.user)
            self.lp.set_password(self.password)
            self.lp.click_button_signin()
            time.sleep(5)
            act_title=self.driver.title
            exp_title="ATS Frontend"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("****Passesd*******")
                    self.lp.click_admin()
                    time.sleep(4)
                    self.lp.click_logout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("****Failed*******")
                    self.lp.click_admin()
                    time.sleep(4)
                    self.lp.click_logout()
                    lst_status.append("Fail")

            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("****Failed*******")
                    self.lp.click_admin()
                    time.sleep(4)
                    self.lp.click_logout()
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("****Passed*******")
                    self.lp.click_admin()
                    time.sleep(4)
                    self.lp.click_logout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("****Login DDT tets passed*******")
            self.driver.close()
            assert True
        else:
            self.logger.info("****Login DDT tets failed*******")
            self.driver.close()
            assert False
        self.logger.info("**** end of Login DDT tets passed*******")
