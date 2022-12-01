from Utility.edit_users_list import Edit_user_list
from selenium.webdriver.common.by import By
import time

class Edit_Fav_Things(Edit_user_list):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)
        self.EU=Edit_user_list(self.driver)

    my_list = (By.XPATH, "//p[normalize-space()='My Lists']")
    fav_things = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/p[1]")
    share_list_button=(By.XPATH,"//div[@class='ShareButton__ShareRect-sc-wu3abh-0 dJUudA']")

    def edit_path(self):
        self.EF.find_element(self.my_list).click()
        self.EF.find_element(self.fav_things).click()
        self.EF.find_element(self.list_edit).click()

    def check_comment(self,comment):
        self.EF.find_element(self.my_list).click()
        self.EU.click_comment(comment)

    def check_edit_fav(self,name,details):
        self.edit_path()
        self.EU.edit_fave(name,details)

    def check_copy_fav(self):
        self.EU.copy_a_fave()

    def check_archive(self):
        self.EU.click_archive()

    def restore_fave_to_list(self):
        self.EU.restore_fave()

    def add_new_fave(self,search,text):
        self.edit_path()
        self.EU.add_a_new_fav(search,text)

    def check_preview_and_share_to(self):
        self.edit_path()
        self.EU.click_preview_list_and_share_to()

    def check_share_list(self):
        self.EF.find_element(self.my_list).click()
        self.EF.find_element(self.fav_things).click()
        time.sleep(3)
        self.EF.find_element(self.share_list_button)
        time.sleep(3)
        self.EU.share_list()







