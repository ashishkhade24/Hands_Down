import time
from pages.edit_profile import Edit_Profile
from page_objects.comftest import setup
import pytest

@pytest.mark.usefixtures("setup")
class Test_Password:

    @pytest.mark.sanity
    def test_reset_password(self):
        obj = Edit_Profile(self.driver)
        obj.password_change("Ashish@1105","Ashish@1105","Ashish@1105")
        time.sleep(3)
        self.driver.save_screenshot("./testdata/screenshot/edit_password/successfully_changed.png")

    def test_wrong_password(self):
        obj = Edit_Profile(self.driver)
        obj.password_change("Ashish@1105", "ashish@1105", "ashish@1105")
        time.sleep(3)
        self.driver.save_screenshot("./testdata/screenshot/edit_password/wrong_pass.png")

    def test_mismatch_password(self):
        obj = Edit_Profile(self.driver)
        obj.password_change("Ashish@1105", "Ashish@1105", "ashish@1105")
        time.sleep(3)
        self.driver.save_screenshot("./testdata/screenshot/edit_password/mismatched_pass.png")

    @pytest.mark.sanity
    def test_empty_field(self):
        obj = Edit_Profile(self.driver)
        obj.password_change("Ashish@1105", " ", "ashish@1105")
        time.sleep(3)
        self.driver.save_screenshot("./testdata/screenshot/edit_password/empty_field.png")








