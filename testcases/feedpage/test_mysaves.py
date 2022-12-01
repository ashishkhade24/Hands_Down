from pages.my_saves import My_Saves
import pytest
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_My_Saves:

    def test_explore_button(self):
        obj=My_Saves(self.driver)
        obj.check_explore_button()

    def test_share_link(self):
        obj = My_Saves(self.driver)
        obj.check_share_links()

    def test_copy_link(self):
        obj = My_Saves(self.driver)
        obj.check_copy_link()

    def test_back_arrow(self):
        obj = My_Saves(self.driver)
        obj.check_back_arrow()

    def test_edit(self):
        obj = My_Saves(self.driver)
        obj.check_edit_func("Ashish","Khade","Bhopal","Quality Analyst")

    def test_invite_friend_valid_email(self):
        obj = My_Saves(self.driver)
        obj.check_invite_friend("testashish22@mailinator.com")

    @pytest.mark.xfail
    def test_invite_friend_invalid_email(self):
        obj = My_Saves(self.driver)
        obj.check_invite_friend("testashish22@gmailcom")

    def test_followers(self):
        obj = My_Saves(self.driver)
        obj.check_followers("mahesh")

    def test_following(self):
        obj = My_Saves(self.driver)
        obj.check_following("mahesh")

    @pytest.mark.sanity
    def test_saves_and_archive(self):
        obj = My_Saves(self.driver)
        obj.check_save_and_archive()



