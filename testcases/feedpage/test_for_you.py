from pages.for_you import ForYou
import pytest
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_For_you:

    def test_for_you_page(self):

        obj=ForYou(self.driver)
        obj.check_all()

