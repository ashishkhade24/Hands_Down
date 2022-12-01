from pages.for_you import ForYou
import pytest
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_For_you:

    def test_button_click(self):

        obj=ForYou(self.driver)
        obj.button_check()

    def test_ele_length(self):
        obj = ForYou(self.driver)
        obj.ele_check()

    def test_first_user(self):
        obj = ForYou(self.driver)
        obj.first_user()

    def test_click_on_first_user(self):
        obj = ForYou(self.driver)
        obj.click_first_user()




