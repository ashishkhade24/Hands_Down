from selenium.webdriver.common.by import By
from page_objects.base import Base
import time

class Suggested_Users(Base):

    def __init__(self,driver):
        self.driver= driver
        super().__init__(driver)

    users=(By.XPATH,"//p[normalize-space()='Jenna Sereni']")
    followers=(By.XPATH,"//p[normalize-space()='Followers']")
    following=(By.XPATH,"//p[normalize-space()='Following']")
    users_follow_button=(By.XPATH,"//button[normalize-space()='Follow']")
    first_follow_button=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
    second_follow_button=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button[1]")
    fourth_follow_button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[4]/div[1]/button[1]")
    invite_friend=(By.XPATH,"//button[normalize-space()='Invite Friends to HandsDown!']")
    enter_email=(By.XPATH,"//input[@id='downshift-multiple-input']")
    send_invite=(By.XPATH,"//button[normalize-space()='Send Invite!']")
    close_button=(By.XPATH,"//button[normalize-space()='Close & Explore More!']")

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

    def click_follow_buttons(self):
        self.EF.find_element(self.first_follow_button).click()
        time.sleep(1)
        self.EF.find_element(self.second_follow_button).click()
        time.sleep(1)
        self.EF.find_element(self.fourth_follow_button).click()
        time.sleep(1)

    def invite_a_friend(self,email):
        self.EF.find_element(self.invite_friend).click()
        self.EF.find_element(self.enter_email).send_keys(email)
        click_button=self.EF.find_element(self.send_invite)
        print(click_button.is_enabled())
        click_button.click()
        self.EF.find_element(self.close_button).click()











