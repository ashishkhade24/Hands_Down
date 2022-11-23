from selenium.webdriver.common.by import By
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

test_data = [
               ["testashish@mailinator.com", "Ashish@1105"],
               ["testashish@mailinator.com", "Ashish@1105"],
               ["testashish@mailinator.com", "Ashish@1105"],
               ["testashish@mailinator.com", "Ashish@1105"],
               ["testashish@mailinator.com", "Ashish@1105"],
               ["testashish@mailinator.com", "Ashish@1105"],
               ["testashish@mailinator.com", "Ashish@1105"],
               ["testashish@mailinator.com", "Ashish@1105"],
               ["testashish@mailinator.com", "Ashish@1105"],
               ["testashish@mailinator.com", "Ashish@1105"]
           ]

@pytest.mark.parametrize("username,password",test_data)
def test_multiple_login(username,password):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://dev.itshandsdown.com/login")
    driver.maximize_window()
    time.sleep(3)
    user_name= driver.find_element(By.XPATH,"//input[contains(@name,'email')]")
    user_name.send_keys(Keys.CONTROL+"a")
    time.sleep(3)
    user_name.send_keys(Keys.BACKSPACE)
    user_name.send_keys(username)
    pass_word=driver.find_element(By.XPATH,"//input[contains(@name,'password')]")
    pass_word.send_keys(Keys.CONTROL+"a")
    time.sleep(3)
    pass_word.send_keys(Keys.BACKSPACE)
    pass_word.send_keys(password)
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    driver.close()
    driver.quit()












