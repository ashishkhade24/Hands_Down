from pages.suggest_user import Suggested_Users
from page_objects.comftest import setup
import pytest

@pytest.mark.usefixtures("setup")
class Test_Suggest_users:

    @pytest.mark.skip
    def test_user_click(self):
        obj=Suggested_Users(self.driver)
        obj.user_search()

    @pytest.mark.skip
    def test_all_buttons(self):
        obj = Suggested_Users(self.driver)
        obj.click_follow_buttons()

    def test_invite_friend_valid_email(self):
        obj = Suggested_Users(self.driver)
        obj.invite_a_friend("test667@mailinator.com")

    @pytest.mark.xfail
    def test_invite_friend_invalid_email(self):
        obj = Suggested_Users(self.driver)
        obj.invite_a_friend("test667@mailinar.")







