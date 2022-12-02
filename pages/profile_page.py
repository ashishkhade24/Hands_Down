from Utility.common_base import Base_Features
class Profile(Base_Features):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)
        self.BF = Base_Features(self.driver)

    def invite_new_friend(self,email):
        self.click_on_name()
        self.BF.invite_a_friend(email)

    def check_share_link(self):
        self.click_on_name()
        self.BF.share_link()

    def check_back_arrow(self):
        self.click_on_name()
        self.BF.back_arrow_check()

    def check_follower(self,name):
        self.click_on_name()
        self.BF.followers_section(name)

    def check_following(self,name):
        self.click_on_name()
        self.BF.following_section(name)

    def check_saves_archive(self):
        self.click_on_name()
        self.BF.click_saves_archive()

    def edit_profile(self,first_name,lastname,city_name,designation):
        self.click_on_name()
        self.BF.check_edit_profile(first_name,lastname,city_name,designation)

    def create_a_new_list(self,list_name):
        self.click_on_name()
        self.BF.create_new_list(list_name)
        self.EF.find_element(self.view_list).click()

    def create_list_with_no_name_category(self, list_name):
        self.click_on_name()
        self.BF.create_list_without_name_category(list_name)

    def check_list_cancel_button(self):
        self.click_on_name()
        self.BF.click_cancel_list_button()

    def create_list_with_fave(self, list_name, search, text):
        self.click_on_name()
        self.BF.create_list_and_add_fave(list_name, search, text)



























