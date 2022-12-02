from pages.profile_page import Profile
from page_objects.comftest import setup
import pytest

@pytest.mark.usefixtures("setup")
class Test_Profile:

    def test_invite_friend_valid_mail(self):
        obj=Profile(self.driver)
        obj.invite_new_friend("testashish444@mailinator.com")

    def test_invite_friend_invalid_mail(self):
        obj=Profile(self.driver)
        obj.invite_new_friend("test344@.cpm")

    def test_share_link(self):
        obj = Profile(self.driver)
        obj.check_share_link()

    def test_back_arrow(self):
        obj = Profile(self.driver)
        obj.check_back_arrow()

    def test_check_follower(self):
        obj=Profile(self.driver)
        obj.check_follower("Dev")

    def test_check_following(self):
        obj=Profile(self.driver)
        obj.check_following("mahesh")

    def test_edit_profile(self):
        obj = Profile(self.driver)
        obj.edit_profile("Ashish","Khade","Bhopal","Quality Analyst")

    def test_save_archive(self):
        obj=Profile(self.driver)
        obj.check_saves_archive()

    def test_new_list(self):
        obj=Profile(self.driver)
        obj.create_a_new_list("Sports")

    @pytest.mark.sanity
    def test_list_without_name_category(self):
        obj = Profile(self.driver)
        obj.create_list_with_no_name_category(" ")

    def test_list_cancel_button(self):
        obj = Profile(self.driver)
        obj.check_list_cancel_button()

    def test_nwe_list_and_add_fave(self):
        obj = Profile(self.driver)
        obj.create_list_with_fave("Flag","India","Pride")








