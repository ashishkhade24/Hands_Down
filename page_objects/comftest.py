import time
import pytest
from page_objects import login_details
from selenium.webdriver.common.by import By
from selenium import webdriver

#Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#Firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#Edge
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

#Chrome
options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
options.add_experimental_option("prefs", prefs)

#Firefox
# options = webdriver.FirefoxOptions()
# options.set_preference('dom.webnotifications.enabled', False)

#Edge
# options = webdriver.EdgeOptions()
# Prefs=("profile.default_content_setting_values.notifications", 2)
# options.set_capability("prefs",Prefs)

username=login_details.USERNAME
password=login_details.PASSWORD

@pytest.fixture(scope="function")
def setup(request):
    browser = "chrome"
    if browser.lower() == "chrome":

        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    elif browser.lower() == "firefox":
        driver = webdriver.Firefox(options=options, service=FirefoxService(GeckoDriverManager().install()))

    else:
        driver = webdriver.Edge(options=options, service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.get("https://dev.itshandsdown.com/login")
    driver.maximize_window()
    driver.find_element(By.NAME, "email").send_keys(username)
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys(password)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(1)
    request.cls.driver = driver

