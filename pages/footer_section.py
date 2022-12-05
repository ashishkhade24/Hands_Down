from Utility.common_footer_file import Footer_Page_Check
import time

class Footer_tabs_check(Footer_Page_Check):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def common_path(self):
        self.click_on_drop_down()
        self.click_on_my_profile()
        self.click_on_how_it_works()

    def check_header_tabs(self):
        self.common_path()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        self.click_on_header_tabs()
        time.sleep(2)
        self.click_on_login_button()
        time.sleep(2)
        self.click_on_join_now_button()

    def check_footer_logo_and_link(self):
        self.common_path()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        self.footer_logo_and_links()

    def check_footer_links(self):
        self.common_path()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        self.click_footer_links()

    def check_contact_us(self,name,email,message):
        self.common_path()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        self.contact_us(name,email,message)

