import pytest
from pages.my_profile import My_Profile
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_My_List:

    def test_links(self):
        obj=My_Profile(self.driver)
        obj.check_share_link()

    def test_copy_link(self):
        obj = My_Profile(self.driver)
        obj.check_copy_link()

    def test_back_arrow(self):
        obj = My_Profile(self.driver)
        obj.check_back_arrow()

    @pytest.mark.sanity
    def test_edit_button_profile(self):
        obj = My_Profile(self.driver)
        obj.check_edit_func("Ashish","Khade","Bhopal","Quality Analyst")

    def test_invite_valid_id(self):
        obj = My_Profile(self.driver)
        obj.check_invite_friend("test1234@mailinator.com")

    @pytest.mark.xfail
    def test_invite_invalid_id(self):
        obj = My_Profile(self.driver)
        obj.check_invite_friend("test1234@mailinator")

    def test_followers(self):
        obj = My_Profile(self.driver)
        obj.check_followers("Mahesh")

    def test_following(self):
        obj = My_Profile(self.driver)
        obj.check_following("Mahesh")

    def test_saves_archive(self):
        obj = My_Profile(self.driver)
        obj.check_save_archive()

    def test_create_list(self):
        obj = My_Profile(self.driver)
        obj.create_list("Books")

    def test_create_list_and_add_fave(self):
        obj = My_Profile(self.driver)
        obj.create_list_with_fave("Nation","India","Pride")

    def test_create_list_without_name_category(self):
        obj = My_Profile(self.driver)
        obj.create_list_with_no_name_category(" ")

    def test_list_cancel_button(self):
        obj = My_Profile(self.driver)
        obj.check_list_cancel_button()

