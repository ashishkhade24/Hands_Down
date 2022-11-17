from selenium.webdriver.common.by import By
from page_objects.base import Base
import time

class ForYou(Base):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div")
    complete_feed = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
    element_count = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/div")
    image_find = (By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")

    def button_check(self):
        buttons= self.EF.find_element(self.button)
        for button in buttons:
            button.click()
            print(button.text)
            time.sleep(1)

    def ele_check(self):
        self.EF.find_element(self.complete_feed)
        ele=self.EF.find_element(self.element_count)
        time.sleep(3)
        print(len(ele))
        time.sleep(3)

    def first_user(self):
        element= self.EF.find_element(self.image_find).is_displayed()
        print(element)
        self.driver.save_screenshot("./testdata/Screenshot/feed_page/image_check.png")








