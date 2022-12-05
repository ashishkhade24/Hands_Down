import pytest
from pages.users_profile import Check_Profile
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_Profile_Check:

    @pytest.mark.sanity
    def test_followers(self):
        obj=Check_Profile(self.driver)
        obj.check_followers_section("ashish")

    def test_following(self):
        obj = Check_Profile(self.driver)
        obj.check_following_section("ayushi")

    def test_edit_profile(self):
        obj = Check_Profile(self.driver)
        obj.edit_users_profile("Ashish","Khade","Bhopal","Quality Analyst")

    def test_comment_section(self):
        obj = Check_Profile(self.driver)
        obj.check_comment("Hero")

    def test_edit_fave(self):
        obj = Check_Profile(self.driver)
        obj.check_edit_fave("Virat Kohli","No recommendation")
        obj.check_copy_fave()
        obj.check_archive_fave()

    def test_restore_fave(self):
        obj= Check_Profile(self.driver)
        obj.restore_fave_to_list()

    def test_add_new_fave(self):
        obj = Check_Profile(self.driver)
        obj.add_new_fave("India","Pride")

    def test_share_list(self):
        obj = Check_Profile(self.driver)
        obj.check_share_list()

    def test_preview_and_share_to(self):
        obj = Check_Profile(self.driver)
        obj.check_preview_and_share_to()




