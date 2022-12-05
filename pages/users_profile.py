import pytest

from Utility.common_base import Base_Features
from selenium.webdriver.common.by import By
from Utility.edit_users_list import Edit_user_list
import time
class Check_Profile(Base_Features):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)
        self.BF = Base_Features(self.driver)
        self.EU = Edit_user_list(self.driver)

    action_button = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]")
    edit_list = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[1]/p[1]")
    share_list_button = ( By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/div[1]/div[2]/p[1]")
    Add_New_Fave = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]")

    def edit_button_and_list(self):
        self.EF.find_element(self.action_button).click()
        self.EF.find_element(self.edit_list).click()

    def share_list_path(self):
        self.EF.find_element(self.action_button).click()
        self.EF.find_element(self.share_list_button).click()

    def check_followers_section(self,name):
        self.BF.followers_section(name)

    def check_following_section(self,name):
        self.BF.following_section(name)

    def edit_users_profile(self,first_name,lastname,city_name,dob,designation):
        self.check_edit_profile(first_name,lastname,city_name,dob,designation)

    def check_comment(self, comment):
        self.EU.click_comment(comment)

    def check_edit_fave(self,name,details):
        self.edit_button_and_list()
        self.EU.edit_fave(name,details)

    def check_copy_fave(self):
        self.EU.copy_a_fave()

    def check_archive_fave(self):
        self.EU.click_archive()

    def restore_fave_to_list(self):
        self.EU.restore_fave()

    def check_preview_and_share_to(self):
        self.edit_button_and_list()
        self.EU.click_preview_list_and_share_to()

    def add_new_fave(self, search, text):
        self.edit_button_and_list()
        self.EU.add_a_new_fav(search, text)

    def check_share_list(self):
        self.share_list_path()
        self.EU.share_list()















