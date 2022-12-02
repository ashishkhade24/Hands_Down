import pytest
from pages.footer_tabs import Check_Footer
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_Footer:

    @pytest.mark.sanity
    def test_logo_and_social_link(self):
        obj=Check_Footer(self.driver)
        obj.check_logo_and_social_links()

    def test_feed_tab(self):
        obj = Check_Footer(self.driver)
        obj.check_feed()

    def test_privacy_tab(self):
        obj = Check_Footer(self.driver)
        obj.check_privacy_policy()

    def test_how_it_works_tab(self):
        obj = Check_Footer(self.driver)
        obj.check_how_it_works()

    def test_terms_of_use(self):
        obj = Check_Footer(self.driver)
        obj.check_terms_of_use()

