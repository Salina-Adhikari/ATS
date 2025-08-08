from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from selenium.webdriver.common.by import By


class users_management:
    usermanagement_link_xpath="//span[contains(., 'User Management')]"
    users_link_xpath="//a[@href='/user-management/users']"
    user_create_xpath="//span[normalize-space()='Create']"
    user_create_photo_xpath="//input[@id='user-image']"
    user_create_username_xpath="//input[@id='username']"
    user_create_email_xpath="//input[@id='email']"
    user_create_phonenumber_xpath="//input[@id='phone']"
    user_create_password_xpath="//input[@id='password']"
    user_create_select_xpath="//select[@id='roleIds']"
    user_create_selectadmin_xpath="//option[@value='46ba7535-10f3-4efc-bc8a-55a60bc6e425']"
    user_create_selecthr_xpath="//option[@value='abdd92ef-bdbb-4fd1-a50d-ad5ecace667d']"
    user_create_selectEmployee_xpath="//option[@value='6d469a33-5870-4935-95c5-37d4020b94f2']"
    user_create_select_head_xpath="//option[@value='2b7c9d7a-0a13-424e-8e6c-86488367afb7']"
    user_create_upload_xpath="//button[normalize-space()='Upload']"
    def __init__(self,driver):
        self.driver = driver
        self.wait=WebDriverWait(self.driver,10)
    def click_user_link(self):
        self.dropdown_button = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.usermanagement_link_xpath)))
        self.dropdown_button.click()
    def click_users_link(self):
        self.option = self.wait.until(EC.element_to_be_clickable((By.XPATH,self.users_link_xpath)))
        self.option.click()

    def click_create_link(self):
        self.driver.find_element(By.XPATH,self.user_create_xpath).click()
    def set_usermanagement_photo(self,photo):
        self.driver.find_element(By.XPATH, self.user_create_upload_xpath).send_keys(photo)
    def set_usermanagement_username(self,username):
        self.driver.find_element(By.XPATH,self.user_create_username_xpath).send_keys(username)
    def set_usermanagement_email(self,email):
        self.driver.find_element(By.XPATH,self.user_create_email_xpath).send_keys(email)
    def set_usermanagement_phonenumber(self,phonenumber):
        self.driver.find_element(By.XPATH,self.user_create_phonenumber_xpath).send_keys(phonenumber)
    def set_usermanagement_password(self,password):
        self.driver.find_element(By.XPATH,self.user_create_password_xpath).send_keys(password)
    def set_usermanagement_roles(self,role):
        self.driver.find_element(By.XPATH,self.user_create_select_xpath)
        if role=="Admin":
            self.listitem=self.driver.find_element(By.XPATH,self.user_create_selectadmin_xpath)
        elif role=="User":
            self.listitem=self.driver.find_element(By.XPATH,self.user_create_selectadmin_xpath)
        elif role=="Employee":
            self.listitem=self.driver.find_element(By.XPATH,self.user_create_selectEmployee_xpath)
        elif role=="Head":
            self.listitem=self.driver.find_element(By.XPATH,self.user_create_select_head_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.user_create_selectadmin_xpath)

        self.listitem.click()

    def click_uploadbutton(self):
        self.driver.find_element(By.XPATH,self.user_create_upload_xpath).click()

