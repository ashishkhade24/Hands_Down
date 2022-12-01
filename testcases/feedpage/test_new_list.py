from pages.check_new_list import Edit_New_List
import pytest
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_New_list:

    def test_add_new_fave(self):
        obj=Edit_New_List(self.driver)
        obj.add_fave("India","pride")
