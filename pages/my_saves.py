from Utility.common_base import Base_Features
from selenium.webdriver.common.by import By

class My_Saves(Base_Features):

    def __init__(self,driver):
        self.driver=driver
        self.BF=Base_Features(self.driver)
        super().__init__(driver)

    my_saves=(By.XPATH,"//p[normalize-space()='My Saves']")
    list=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[1]/p[1]")
    explore_feed = (By.XPATH, "//button[normalize-space()='Explore Feed Now']")

    def check_explore_button(self):
        self.EF.find_element(self.my_saves).click()
        self.EF.find_element(self.explore_feed).click()

    def check_share_links(self):
        self.EF.find_element(self.my_saves).click()
        self.BF.share_link()

    def check_copy_link(self):
        self.EF.find_element(self.my_saves).click()
        self.BF.copy_the_link()

    def check_back_arrow(self):
        self.EF.find_element(self.my_saves).click()
        self.BF.back_arrow_check()

    def check_edit_func(self,first_name,lastname,city_name,designation):
        self.EF.find_element(self.my_saves).click()
        self.BF.check_edit_profile(first_name,lastname,city_name,designation)

    def check_invite_friend(self, email):
        self.EF.find_element(self.my_saves).click()
        self.BF.invite_a_friend(email)

    def check_followers(self, name):
        self.EF.find_element(self.my_saves).click()
        self.BF.followers_section(name)

    def check_following(self, name):
        self.EF.find_element(self.my_saves).click()
        self.BF.following_section(name)

    def check_save_and_archive(self):
        self.EF.find_element(self.my_saves).click()
        self.EF.find_element(self.list).click()
        self.BF.click_saves_archive()






