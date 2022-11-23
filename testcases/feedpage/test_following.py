from pages.following import Following_Page
import pytest
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_Following:

    def test_like_button(self):
        obj=Following_Page(self.driver)
        obj.like_click()

