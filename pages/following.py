from page_objects.base import Base
import time
from selenium.webdriver.common.by import By

class Following_Page(Base):

    def __init__(self,driver):
        self.driver= driver
        super().__init__(self.driver)

    following_button=(By.XPATH,"//a[normalize-space()='Following']")
    complete_page= (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]")
    # like_button= (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]")
    like=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]")

    def like_click(self):
        self.EF.find_element(self.following_button).click()
        self.EF.find_element(self.complete_page)
        self.EF.find_element(self.like).click()
        time.sleep(3)
        self.driver.save_screenshot("./testdata/screenshot/like_click2.png")



