from selenium.webdriver.common.by import By
import time
from page_objects.base import Base
from selenium.webdriver.common.keys import Keys

class Login(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    user_name=(By.NAME, "email")
    pass_word=(By.NAME, "password")
    enter_button=(By.XPATH, "//button[normalize-space()='Login']")
    page=(By.XPATH,"//div[@class='sc-dkrFOg gzTsAp']")
    forgotPass =(By.XPATH,"//p[@class='Text__Label-sc-4on308-0 bySHRv']")
    enter_email=(By.XPATH,"//input[contains(@name,'email')]")
    log_button=(By.XPATH,"//button[normalize-space()='Submit']")

    def input_username(self,username):
        self.EF.find_element(self.user_name).send_keys(username)

    def input_password(self,password):
        self.EF.find_element(self.pass_word).send_keys(password)

    def enter(self):
        self.EF.find_element(self.enter_button).click()
        time.sleep(5)

    def forgot_pass_correct(self):
        self.EF.find_element(self.forgotPass).click()
        time.sleep(5)
        self.EF.find_element(self.enter_email).send_keys("test66@mailinator.com")
        self.EF.find_element(self.log_button).click()
        time.sleep(5)

    def forgot_pass_incorrect(self):
        self.EF.find_element(self.forgotPass).click()
        time.sleep(5)
        self.EF.find_element(self.enter_email).send_keys("test66@mailinator.c")
        self.EF.find_element(self.log_button).click()
        time.sleep(5)

















