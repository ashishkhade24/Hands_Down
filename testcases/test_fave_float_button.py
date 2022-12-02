from page_objects.comftest import setup
import pytest
from pages.fave_floating_button import Add_a_fave

@pytest.mark.usefixtures("setup")
class Test_Add_A_New_Fave:

    def test_add_fave(self):
        obj=Add_a_fave(self.driver)
        obj.add_a_fave("India","Pride")

    @pytest.mark.sanity
    def test_cut_button(self):
        obj = Add_a_fave(self.driver)
        obj.check_cut_button("India", "Pride")

