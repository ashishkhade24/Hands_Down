import pytest
from pages.users_profile import Check_Profile
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_Profile:

    def test_followers(self):
        obj=Check_Profile(self.driver)
        obj.followers_section("ashish")

    @pytest.mark.sanity
    def test_following(self):
        obj = Check_Profile(self.driver)
        obj.following_section("ayushi")
