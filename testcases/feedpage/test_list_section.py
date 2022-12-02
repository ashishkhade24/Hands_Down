from pages.edit_list_section import Edit_Fav_Things
import pytest
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_Favourite_Things:

    def test_comment_section(self):
        obj = Edit_Fav_Things(self.driver)
        obj.check_comment("Attitude_killer")

    def test_edit_fave(self):
        obj=Edit_Fav_Things(self.driver)
        obj.check_edit_fav("Virat Kohli", "No recommendation")
        obj.check_copy_fav()
        obj.check_archive()

    def test_restore_fave(self):
        obj = Edit_Fav_Things(self.driver)
        obj.restore_fave_to_list()

    def test_add_fave(self):
        obj = Edit_Fav_Things(self.driver)
        obj.add_new_fave("India","pride")

    def test_share_list(self):
        obj = Edit_Fav_Things(self.driver)
        obj.check_share_list()

    def test_preview_and_share_to(self):
        obj = Edit_Fav_Things(self.driver)
        obj.check_preview_and_share_to()




