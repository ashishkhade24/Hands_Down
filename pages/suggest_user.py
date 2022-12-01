from selenium.webdriver.common.by import By
import time
from Utility.common_base import Base_Features

class Suggested_Users(Base_Features):

    def __init__(self,driver):
        self.driver= driver
        super().__init__(driver)
        self.BF = Base_Features(self.driver)

    users=(By.XPATH,"//p[normalize-space()='Jenna Sereni']")
    followers=(By.XPATH,"//p[normalize-space()='Followers']")
    following=(By.XPATH,"//p[normalize-space()='Following']")
    users_follow_button=(By.XPATH,"//button[normalize-space()='Follow']")
    first_follow_button=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
    second_follow_button=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]")
    fourth_follow_button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]")

    def user_search(self):
        self.EF.find_element(self.users).click()
        time.sleep(2)
        self.EF.find_element(self.followers).click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.EF.find_element(self.following).click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.EF.find_element(self.users_follow_button).click()
        time.sleep(2)
        self.driver.quit()

    def click_follow_buttons(self):
        self.EF.find_element(self.first_follow_button).click()
        time.sleep(1)
        self.EF.find_element(self.second_follow_button).click()
        time.sleep(1)
        self.EF.find_element(self.fourth_follow_button).click()
        time.sleep(1)
        self.driver.quit()

    def check_invite_friend(self,email):
        self.BF.invite_a_friend(email)














