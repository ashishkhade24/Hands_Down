from pages.edit_profile import Edit_Profile
from page_objects.comftest import setup
import pytest

@pytest.mark.usefixtures("setup")
class Test_Edits:

    def test_last_name_edit(self):
        obj=Edit_Profile(self.driver)
        obj.edit_last_name("Khade")

    def test_edit_location(self):
        obj = Edit_Profile(self.driver)
        obj.edit_location("Bhopal")

    def test_bio_edit(self):
        obj = Edit_Profile(self.driver)
        obj.edit_bio("Quality Analyst")

    @pytest.mark.sanity
    def test_edit_categories(self):
        obj = Edit_Profile(self.driver)
        obj.edit_categories()

    def test_email_preference(self):
        obj = Edit_Profile(self.driver)
        obj.email_preference()




