from page_objects.base import Base
from selenium.webdriver.common.by import By
import time

class Check_Profile(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    followers=(By.XPATH,"//p[normalize-space()='Followers']")
    following=(By.XPATH,"//p[normalize-space()='Following']")
    back_button_follower=(By.XPATH,"//h1[contains(@class,'Text__H1-sc-4on308-1 fqthkj')]")
    back_button_following=(By.XPATH,"//h1[contains(@class,'Text__H1-sc-4on308-1 fqthkj')]")
    find_someone=(By.XPATH,"//input[@placeholder='Find someone']")
    all_followers=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div")
    user_click=(By.XPATH,"//p[normalize-space()='Dev Mahesh']")
    unfollow=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[9]/button[1]")
    view_more=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/p[1]")

    def followers_section(self,name):
        self.EF.find_element(self.followers).click()
        self.EF.find_element(self.find_someone).send_keys(name)
        time.sleep(2)
        self.EF.find_element(self.back_button_follower).click()
        self.driver.quit()

    def following_section(self,name):
        self.EF.find_element(self.following).click()
        self.EF.find_element(self.find_someone).send_keys(name)
        time.sleep(2)
        self.driver.refresh()
        self.EF.find_element(self.view_more).click()
        # list_of_people= self.EF.find_element(self.all_followers)
        # print(len(list_of_people))
        self.EF.find_element(self.user_click).click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.EF.find_element(self.unfollow).click()
        time.sleep(2)
        self.EF.find_element(self.back_button_following).click()
        self.driver.quit()
















