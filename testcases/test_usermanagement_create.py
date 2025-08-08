import time
from selenium.webdriver.common.by import By
import pytest

from pageobjects.UsersManagement import users_management
from utilities.customLogger import  LogGen
from utilities.readProperties import ReadConfig
from pageobjects.LoginPage import LoginPage
class Test_2_UserManagemnet():
    url=ReadConfig.getApplicationURL()
    email=ReadConfig.getUseremail()
    password=ReadConfig.getUserpassword()
    photo=ReadConfig.getPhoto()
    username=ReadConfig.getUsername()
    User_email=ReadConfig.getEmail()
    User_phonenumber=ReadConfig.getPhonenummber()
    User_password=ReadConfig.getPassword()
    User_roles=ReadConfig.getRoles()
    logger=LogGen.loggen()
    def test_login(self,setup):
        self.driver=setup
        self.logger.info("Test_2_UserManagement.test_usermanagement")
        self.logger.info("User Management")
        time.sleep(2)
        self.driver.get(self.url)
        self.lp=LoginPage(self.driver)
        self.lp.click_home_signin()
        time.sleep(4)
        self.lp.set_email(self.email)
        self.lp.set_password(self.password)
        time.sleep(2)
        self.lp.click_button_signin()
        time.sleep(10)
        self.um=users_management(self.driver)
        self.um.click_user_link()
        time.sleep(2)
        self.um.click_users_link()
        time.sleep(2)
        self.um.click_create_link()
        self.um.set_usermanagement_photo(self.photo)
        time.sleep(2)
        self.um.set_usermanagement_username(self.username)
        self.um.set_usermanagement_email(self.User_email)
        self.um.set_usermanagement_phonenumber(self.User_phonenumber)
        self.um.set_usermanagement_password(self.User_password)
        self.um.set_usermanagement_roles(self.User_roles)
        self.um.click_user_link()
        self.driver.quit()




