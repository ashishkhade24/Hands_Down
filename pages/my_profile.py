from Utility.common_base import Base_Features

class My_Profile(Base_Features):

    def __init__(self,driver):
        self.driver=driver
        self.BF=Base_Features(self.driver)
        super().__init__(driver)

    def common_path(self):
        self.click_on_drop_down()
        self.click_on_my_profile()

    def check_share_link(self):
        self.common_path()
        self.BF.share_link()

    def check_copy_link(self):
        self.common_path()
        self.BF.copy_the_link()

    def check_back_arrow(self):
        self.common_path()
        self.BF.back_arrow_check()

    def check_edit_func(self,first_name,lastname,city_name,designation):
        self.common_path()
        self.BF.check_edit_profile(first_name,lastname,city_name,designation)

    def check_invite_friend(self, email):
        self.common_path()
        self.BF.invite_a_friend(email)

    def check_followers(self, name):
        self.common_path()
        self.BF.followers_section(name)

    def check_following(self, name):
        self.common_path()
        self.BF.following_section(name)

    def check_save_archive(self):
        self.common_path()
        self.BF.click_saves_archive()

    def create_list(self,category):
        self.common_path()
        self.BF.create_new_list(category)

