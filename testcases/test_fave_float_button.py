from page_objects.comftest import setup
import pytest
from pages.fave_floating_button import Add_a_fave

@pytest.mark.usefixtures("setup")
class Test_Add_A_New_Fave:

    def test_add_fave(self):
        obj=Add_a_fave(self.driver)
        obj.add_a_fave("India","Pride")

    def test_cut_button(self):
        obj = Add_a_fave(self.driver)
        obj.check_cut_button("India", "Pride")

    def test_lets_keep_at_this(self):
        obj = Add_a_fave(self.driver)
        obj.check_lets_keep_at_this("India", "Pride")

    @pytest.mark.sanity
    def test_done_for_now(self):
        obj = Add_a_fave(self.driver)
        obj.check_done_for_now()

