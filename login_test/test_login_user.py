import unittest
from page_objects.login import Login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class Test_LogIN(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://dev.itshandsdown.com/login")
        self.driver.maximize_window()

    def test_valid_credentials(self):

        lg=Login(self.driver)
        lg.input_username("testashish@mailinator.com")
        lg.input_password("Ashish@1105")
        lg.enter()

    def test_invalid_username(self):
        lg=Login(self.driver)
        lg.input_username("testashish@mailinator.")
        lg.input_password("Ashish@1105")
        lg.enter()
        # self.driver.save_screenshot("./testdata/Screenshot/test_invalid_user_.png")

    def test_invalid_password(self):
        lg = Login(self.driver)
        lg.input_username("testashish@mailinator.com")
        lg.input_password("Ashish@11")
        lg.enter()
        # self.driver.save_screenshot("./testdata/Screenshot/test_invalid_pass_.png")

    def test_empty_field(self):
        lg = Login(self.driver)
        lg.input_username("testashish@mailinator.com")
        lg.input_password("")
        lg.enter()
        self.driver.save_screenshot("./testdata/Screenshot/login_empty_field.png")

    def test_forgot_password_valid_mail(self):
        lg = Login(self.driver)
        lg.forgot_pass_correct()
        # self.driver.save_screenshot("./testdata/Screenshot/otp_sent.png")

    def test_forgot_password_invalid_mail(self):
        lg = Login(self.driver)
        lg.forgot_pass_incorrect()
        # self.driver.save_screenshot("./testdata/Screenshot/error_msg.png")

    def tearDown(self) -> None:
        self.driver.quit()
