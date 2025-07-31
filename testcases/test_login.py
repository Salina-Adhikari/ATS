import time
from selenium.webdriver.common.by import By
import pytest
from utilities.customLogger import  LogGen
from utilities.readProperties import ReadConfig
from pageobjects.LoginPage import LoginPage
class Test_1_Login:
    url=ReadConfig.getApplicationURL()
    email=ReadConfig.getUseremail()
    password=ReadConfig.getUserpassword()

    logger=LogGen.loggen()
    def test_login(self,setup):
        self.driver=setup
        self.logger.info("Test_1_Login.test_login")
        self.logger.info("Verifying the Login Page")
        time.sleep(2)
        self.driver.get(self.url)
        self.lp=LoginPage(self.driver)
        self.lp.click_home_signin()
        time.sleep(4)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        time.sleep(2)
        self.lp.click_sigin()
        time.sleep(2)
        self.lp.click_admin()
        time.sleep(2)
        self.lp.click_logout()
        self.driver.quit()



        # message_text=self.lp.capture_login()
        # assert "Login successful" in message_text


