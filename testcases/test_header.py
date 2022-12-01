import time
import pytest
from pages.header import Header_Section
from page_objects.comftest import setup

@pytest.mark.usefixtures("setup")
class Test_Header:

    def test_header_section(self):
        obj=Header_Section(self.driver)
        obj.check_my_list()
        time.sleep(2)
        obj.click_on_my_saves()
        time.sleep(2)
        obj.check_feed()
        time.sleep(2)
        obj.check_notifications()
        time.sleep(2)
        self.driver.back()
        self.driver.quit()

    def test_logout(self):
        obj = Header_Section(self.driver)
        obj.check_logout()
        self.driver.quit()


