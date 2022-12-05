from pages.edit_profile import Edit_Profile
from page_objects.comftest import setup
import pytest

@pytest.mark.usefixtures("setup")
class Test_Edits:

    @pytest.mark.sanity
    def test_edit(self):
        obj=Edit_Profile(self.driver)
        obj.edit_first_name("Ashish")
        obj.edit_last_name("Khade")
        obj.edit_location("Bhopal")
        obj.edit_dob("11/05/1995")
        obj.edit_bio("Quality Analyst")
        obj.edit_categories()
        obj.save_edit()

    def test_email_preference(self):
        obj = Edit_Profile(self.driver)
        obj.email_preference()




