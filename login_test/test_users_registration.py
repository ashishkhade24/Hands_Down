import time
import unittest
from page_objects.registration import Registration
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Test_Register_users(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://dev.itshandsdown.com/login")
        self.driver.maximize_window()

    def test_user_registration(self):
        obj=Registration(self.driver)
        obj.click_singup_link()
        obj.enter_firstname("Ashish")
        obj.enter_lastname("Khade")
        obj.enter_email("test1190@mailinator.com")
        obj.enter_password("Ashish@1105")
        obj.confirm_password("Ashish@1105")
        obj.click_sing_up()
        time.sleep(5)
        self.driver.save_screenshot("./login_test/Testdata/screen_shots/registration_page/registration_done1.png")

    def test_already_used_email(self):
        obj = Registration(self.driver)
        obj.click_singup_link()
        obj.enter_firstname("Ashish")
        obj.enter_lastname("Khade")
        obj.enter_email("test999@mailinator.com")
        obj.enter_password("Ashish@1105")
        obj.confirm_password("Ashish@1105")
        obj.click_sing_up()
        time.sleep(5)
        self.driver.save_screenshot("./login_test/Testdata/screen_shots/registration_page/email_already_exist.png")

    def test_with_wrong_email(self):
        obj = Registration(self.driver)
        obj.click_singup_link()
        obj.enter_firstname("Ashish")
        obj.enter_lastname("Khade")
        obj.enter_email("test@mailinatorcom")
        obj.enter_password("Ashish@1105")
        obj.confirm_password("Ashish@1105")
        obj.click_sing_up()
        time.sleep(5)
        self.driver.save_screenshot("./login_test/Testdata/screen_shots/registration_page/enter_valid_email.png")

    def test_with_wrong_password(self):
        obj = Registration(self.driver)
        obj.click_singup_link()
        obj.enter_firstname("Ashish")
        obj.enter_lastname("Khade")
        obj.enter_email("test111@mailinator.com")
        obj.enter_password("ashish@1105")
        obj.confirm_password("ashish@1105")
        obj.click_sing_up()
        time.sleep(5)
        self.driver.save_screenshot("./login_test/Testdata/screen_shots/registration_page/enter_valid_password1.png")

    def test_mismatch_of_passwords(self):
        obj = Registration(self.driver)
        obj.click_singup_link()
        obj.enter_firstname("Ashish")
        obj.enter_lastname("Khade")
        obj.enter_email("test111@mailinator.com")
        obj.enter_password("Ashish@1105")
        obj.confirm_password("ashish@1105")
        obj.click_sing_up()
        time.sleep(5)
        self.driver.save_screenshot("./login_test/Testdata/screen_shots/registration_page/mis_matched_passwords1.png")

    def test_for_empty_field(self):
        obj = Registration(self.driver)
        obj.click_singup_link()
        obj.enter_firstname(" ")
        obj.enter_lastname("Khade")
        obj.enter_email("test111@mailinator.com")
        obj.enter_password("Ashish@1105")
        obj.confirm_password("Ashish@1105")
        obj.click_sing_up()
        time.sleep(5)
        self.driver.save_screenshot("./login_test/Testdata/screen_shots/registration_page/empty_field1.png")

    def tearDown(self) -> None:
        self.driver.quit()
