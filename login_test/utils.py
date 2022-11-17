from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Elem_fun:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator_tuple):
        try:
            element = WebDriverWait(self.driver, 10, poll_frequency=1).until(
                EC.presence_of_element_located(locator_tuple))
            return element

        except:
            self.driver.save_screenshot("./testdata/Screenshot/test01.png")