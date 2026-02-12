from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:
    # hamburger_icon_css=".lucide.lucide-menu.h-6.w-6"
    button_home_sigin_xpath="//a[@class='text-gray-600 hover:text-blue-600 px-3 py-2 rounded-md text-sm font-medium transition-colors' and @href='/sign-in']"
    textbox_email_xpath="//input[@id='email']"
    textbox_password_id="password"
    button_sigin_xpath="//button[normalize-space()='Sign in']"
    # link_logout_linktext=""
    pop_login_xpath=  "//ol[@dir='ltr']//li"
    admin_button_xpath="//div[@id='profileIcon']//button//p[text()='admin@omega.com']"
    # admin_button_xpath = "nav[class='flex flex-col md:flex-row justify-between items-start md:items-center gap-2 py-4 mb-6 w-full border-b border-gray-200']"

    button_logout_xpath="//button[normalize-space()='Sign out']"


    def __init__(self,driver):
        self.driver=driver
    # def home_hamburger_icon(self):
    #     self.driver.find_element(By.CSS_SELECTOR,self.hamburger_icon_css).click()
    def click_home_signin(self):
        home_signin_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_home_sigin_xpath))
        )
        home_signin_btn.click()

    def set_email(self,email):
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).send_keys(email)

    def set_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def click_button_signin(self):
        home_signin_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_sigin_xpath))
        )
        home_signin_btn.click()

    def click_admin(self):
        admin_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.admin_button_xpath))
        )
        admin_btn.click()

    def click_logout(self):
        logout_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_logout_xpath))
        )
        self.driver.execute_script("arguments[0].click();", logout_btn)

    # def capture_login(self):
    #     try:
    #
    #         element = WebDriverWait(self.driver, 10).until(
    #             EC.visibility_of_element_located((By.XPATH, self.pop_login_xpath))
    #         )
    #         return element.text
    #     except Exception as e:
    #         print("Login message element not interactable or not visible:", str(e))
    #         return ""




