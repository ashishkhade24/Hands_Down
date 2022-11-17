from selenium.webdriver.common.by import By
import time
from login_test.utils import Elem_fun

class Registration:
    def __init__(self,driver):
        self.driver = driver
        self.EF= Elem_fun(self.driver)

    signup_button = (By.XPATH, "//a[normalize-space()='Sign Up']")
    first_name_txt = (By.XPATH, "//input[contains(@name,'first_name')]")
    last_name_txt = (By.XPATH, "//input[contains(@name,'last_name')]")
    email = (By.XPATH, "//input[contains(@name,'email')]")
    pass_word = (By.XPATH, "//input[contains(@name,'password')]")
    confirm_pass = (By.XPATH, "//input[contains(@name,'confirm_password')]")
    submit = (By.XPATH, "//button[normalize-space()='Sign Up']")
    ok_button = (By.XPATH, "//button[normalize-space()='OK']")

    def click_singup_link(self):
        self.EF.find_element(self.signup_button).click()
        time.sleep(5)

    def enter_firstname(self, first_name):
        self.EF.find_element(self.first_name_txt).send_keys(first_name)

    def enter_lastname(self, last_name):
        self.EF.find_element(self.last_name_txt).send_keys(last_name)

    def enter_email(self, mail):
        self.EF.find_element(self.email).send_keys(mail)

    def enter_password(self, password):
        self.EF.find_element(self.pass_word).send_keys(password)

    def confirm_password(self, confirm_p):
        self.EF.find_element(self.confirm_pass).send_keys(confirm_p)

    def click_sing_up(self):
        self.EF.find_element(self.submit).click()

    def click_on_ok(self):
        self.EF.find_element(self.ok_button).click()

