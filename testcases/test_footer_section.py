import pytest
from pages.footer_section import Footer_tabs_check
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_Footer_section:

    def test_new_page_header(self):
        obj=Footer_tabs_check(self.driver)
        obj.check_header_tabs()

    def test_footer_logo_and_links(self):
        obj = Footer_tabs_check(self.driver)
        obj.check_footer_logo_and_link()

    @pytest.mark.sanity
    def test_footer_links(self):
        obj = Footer_tabs_check(self.driver)
        obj.check_footer_links()

    def test_contact_us_section(self):
        obj = Footer_tabs_check(self.driver)
        obj.check_contact_us("Ashish","testashish11@mailinator.com","No Message")
