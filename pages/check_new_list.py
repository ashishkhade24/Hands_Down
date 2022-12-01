from Utility.edit_users_list import Edit_user_list
from selenium.webdriver.common.by import By
import time

class Edit_New_List(Edit_user_list):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)
        self.EU=Edit_user_list(self.driver)

    my_list = (By.XPATH, "//p[normalize-space()='My Lists']")

    def add_fave(self,search,text):
        self.EF.find_element(self.my_list).click()
        self.EU.add_fave_in_new_list(search,text)

    def
