from selenium.webdriver.common.by import By
from page_objects.base import Base
import time

class ForYou(Base):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    all_buttons = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div")
    complete_feed = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]")
    element_count = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div/div/div")
    find_user = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")

    def button_check(self):
        buttons= self.EF.find_elements(self.all_buttons)
        for button in buttons:
            button.click()
            print(button.text)
            time.sleep(1)
        self.driver.refresh()
        time.sleep(3)

    def ele_check(self):
        self.EF.find_element(self.complete_feed)
        time.sleep(4)
        ele=self.EF.find_elements(self.element_count)
        time.sleep(3)
        print(len(ele))
        time.sleep(3)
        self.driver.refresh()

    def first_user(self):
        self.EF.find_element(self.complete_feed)
        element= self.EF.find_element(self.find_user).is_displayed()
        print(element)
        self.driver.save_screenshot("./testdata/Screenshot/feed_page/image_check1.png")
        self.driver.refresh()

    def click_first_user(self):
        self.EF.find_element(self.complete_feed)
        self.EF.find_element(self.find_user).click()
        self.driver.save_screenshot("./testdata/Screenshot/feed_page/user_click1.png")
        self.driver.refresh()

    def check_all(self):
        self.button_check()
        self.ele_check()
        self.first_user()
        self.click_first_user()















