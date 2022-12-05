import pytest
from pages.my_list import My_List
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_My_List:

    def test_links(self):
        obj=My_List(self.driver)
        obj.check_share_links()

    def test_copy_link(self):
        obj = My_List(self.driver)
        obj.check_copy_link()

    def test_back_arrow(self):
        obj = My_List(self.driver)
        obj.check_back_arrow()

    @pytest.mark.sanity
    def test_edit_button(self):
        obj = My_List(self.driver)
        obj.check_edit_button("Ashish","Khade","Bhopal","11/05/1995","Quality Analyst")

    def test_invite_valid_id(self):
        obj = My_List(self.driver)
        obj.check_invite_friend("test1234@mailinator.com")

    @pytest.mark.xfail
    def test_invite_invalid_id(self):
        obj = My_List(self.driver)
        obj.check_invite_friend("test1234@mailinator")

    def test_followers(self):
        obj = My_List(self.driver)
        obj.check_followers("Mahesh")

    def test_following(self):
        obj = My_List(self.driver)
        obj.check_following("Mahesh")

    def test_saves_archive(self):
        obj = My_List(self.driver)
        obj.check_save_and_archive()

    def test_create_list(self):
        obj = My_List(self.driver)
        obj.create_list("Books")

    def test_new_list_and_add_fave(self):
        obj = My_List(self.driver)
        obj.create_list_with_fave("Flag", "India", "Pride")

    def test_cancel_list_button(self):
        obj = My_List(self.driver)
        obj.check_list_cancel_button()

    def test_list_with_no_name(self):
        obj = My_List(self.driver)
        obj.create_list_without_name_category(" ")

