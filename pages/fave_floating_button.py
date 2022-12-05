import pytest
from selenium.webdriver.common.by import By
import time
from page_objects.base import Base
from Utility.edit_users_list import Edit_user_list
from selenium.webdriver.common.keys import Keys

class Add_a_fave(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)
        self.EU=Edit_user_list(self.driver)

    add_fave=(By.XPATH,"//div[@class='FaveFloatingButton__Container-sc-k0chkv-0 hdFcNB']")
    search_text = (By.XPATH, "//input[@placeholder='Search the web or paste a link']")
    wikipedia = (By.XPATH, "//div[normalize-space()='India - Wikipedia']")
    add_fave_category = (By.XPATH, "//div[@id='selector-category']")
    podcast = (By.XPATH, "//li[normalize-space()='Podcasts']")
    add_list = (By.XPATH, "//div[@id='selector-list']")
    click_list = (By.XPATH, "//li[normalize-space()='Nation']")
    comment_text = (By.XPATH, "//textarea[@id='outlined-textarea']")
    publish = (By.XPATH, "//button[normalize-space()='Publish']")
    go_to_list = (By.XPATH, "//button[normalize-space()='Go To List']")
    X_link=(By.XPATH,"//div[@class='FaveLinkSearchModal__HeaderStyled-sc-ag850r-4 kcRquN']/*[local-name()='svg']")
    cut_button=(By.XPATH,"//div[@class='Popup__ContainerCloseIcon-sc-bwbjhr-2 btETSz']/*[local-name()='svg']")
    lets_keep=(By.XPATH,"/html[1]/body[1]/div[4]/div[3]/button[1]")
    yup_done=(By.XPATH,"/html[1]/body[1]/div[4]/div[3]/button[2]")

    def add_a_fave(self,search,text):
        self.EF.find_element(self.add_fave).click()
        time.sleep(3)
        search_things = self.EF.find_element(self.search_text)
        search_things.clear()
        search_things.send_keys(search)
        search_things.send_keys(Keys.ENTER)
        self.EF.find_element(self.wikipedia).click()
        self.EF.find_element(self.add_fave_category).click()
        self.EF.find_element(self.podcast).click()
        self.EF.find_element(self.add_list).click()
        self.EF.find_element(self.click_list).click()
        self.EF.find_element(self.comment_text).send_keys(text)
        self.EF.find_element(self.publish).click()
        time.sleep(2)
        self.EF.find_element(self.go_to_list).click()
        time.sleep(2)
        self.driver.quit()

    def check_cut_button(self,search,text):
        self.EF.find_element(self.add_fave).click()
        time.sleep(3)
        check_x_button= self.EF.find_element(self.X_link)
        check_x_button.click()
        time.sleep(3)
        self.EF.find_element(self.cut_button).click()
        time.sleep(3)
        search_things = self.EF.find_element(self.search_text)
        search_things.clear()
        search_things.send_keys(search)
        search_things.send_keys(Keys.ENTER)
        self.EF.find_element(self.wikipedia).click()
        self.EF.find_element(self.add_fave_category).click()
        self.EF.find_element(self.podcast).click()
        self.EF.find_element(self.add_list).click()
        self.EF.find_element(self.click_list).click()
        self.EF.find_element(self.comment_text).send_keys(text)
        self.EF.find_element(self.publish).click()
        time.sleep(2)
        self.EF.find_element(self.go_to_list).click()
        time.sleep(2)
        self.driver.quit()

    def check_lets_keep_at_this(self,search,text):
        self.EF.find_element(self.add_fave).click()
        time.sleep(3)
        check_x_button = self.EF.find_element(self.X_link)
        check_x_button.click()
        time.sleep(3)
        self.EF.find_element(self.lets_keep).click()
        time.sleep(3)
        search_things = self.EF.find_element(self.search_text)
        search_things.clear()
        search_things.send_keys(search)
        search_things.send_keys(Keys.ENTER)
        self.EF.find_element(self.wikipedia).click()
        self.EF.find_element(self.add_fave_category).click()
        self.EF.find_element(self.podcast).click()
        self.EF.find_element(self.add_list).click()
        self.EF.find_element(self.click_list).click()
        self.EF.find_element(self.comment_text).send_keys(text)
        self.EF.find_element(self.publish).click()
        time.sleep(2)
        self.EF.find_element(self.go_to_list).click()
        time.sleep(2)
        self.driver.quit()

    def check_done_for_now(self):
        self.EF.find_element(self.add_fave).click()
        time.sleep(3)
        check_x_button = self.EF.find_element(self.X_link)
        check_x_button.click()
        time.sleep(3)
        self.EF.find_element(self.yup_done).click()
        time.sleep(3)










