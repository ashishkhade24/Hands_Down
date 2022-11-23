from pages.profile_page import Profile
from page_objects.comftest import setup
import pytest

@pytest.mark.usefixtures("setup")
class Test_Profile:

    @pytest.mark.one
    def test_invite_friend_valid_mail(self):
        obj=Profile(self.driver)
        obj.invite_a_friend("testashish444@mailinator.com")

    def test_invite_friend_invalid_mail(self):
        obj=Profile(self.driver)
        obj.invite_a_friend_invalid_id("test344@.cpm")

    def test_check_follower(self):
        obj=Profile(self.driver)
        obj.check_follower("Dev")

    def test_check_following(self):
        obj=Profile(self.driver)
        obj.check_following()

    def test_save_archive(self):
        obj=Profile(self.driver)
        obj.click_saves_archive()

    @pytest.mark.sanity
    def test_new_list(self):
        obj=Profile(self.driver)
        obj.create_new_list()










