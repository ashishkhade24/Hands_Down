from Utility.common_base import Base_Features

class My_List(Base_Features):

    def __init__(self,driver):
        self.driver=driver
        self.BF=Base_Features(self.driver)
        super().__init__(driver)

    def check_share_links(self):
        self.click_on_my_list()
        self.BF.share_link()

    def check_copy_link(self):
        self.click_on_my_list()
        self.BF.copy_the_link()

    def check_back_arrow(self):
        self.click_on_my_list()
        self.BF.back_arrow_check()

    def check_edit_button(self,first_name,lastname,city_name,designation):
        self.click_on_my_list()
        self.BF.check_edit_profile(first_name,lastname,city_name,designation)

    def check_invite_friend(self,email):
        self.click_on_my_list()
        self.BF.invite_a_friend(email)

    def check_followers(self,name):
        self.click_on_my_list()
        self.BF.followers_section(name)

    def check_following(self,name):
        self.click_on_my_list()
        self.BF.following_section(name)

    def check_save_and_archive(self):
        self.click_on_my_list()
        self.BF.click_saves_archive()

    def create_list(self,list_name):
        self.click_on_my_list()
        self.BF.create_new_list(list_name)
        self.EF.find_element(self.view_list).click()

    def create_list_with_fave(self,list_name,search,text):
        self.click_on_my_list()
        self.BF.create_list_and_add_fave(list_name,search,text)













