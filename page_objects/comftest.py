from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)
from page_objects import login_details

username=login_details.USERNAME
password=login_details.PASSWORD

@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://dev.itshandsdown.com/login")
    driver.maximize_window()
    driver.find_element(By.NAME, "email").send_keys(username)
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(1)
    request.cls.driver = driver
