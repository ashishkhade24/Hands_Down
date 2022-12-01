import pytest
from pages.search import Search
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_search:

    def test_people_search(self):
        obj=Search(self.driver)
        obj.search_people("mahesh")

    def test_slider(self):
        obj = Search(self.driver)
        obj.check_slider("mahesh")

    def test_fave_category(self):
        obj = Search(self.driver)
        obj.check_fave_category("mahesh")

    @pytest.mark.sanity
    def test_cart(self):
        obj = Search(self.driver)
        obj.check_cart("mahesh")
