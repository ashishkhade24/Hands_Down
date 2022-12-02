from Utility.common_footer_file import Footer_Page_Check
import time

class Check_Footer(Footer_Page_Check):

    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def my_profile(self):
        self.click_on_drop_down()
        self.click_on_my_profile()

    def check_logo_and_social_links(self):
        self.my_profile()
        time.sleep(3)
        self.click_on_logo_and_social_link()

    def check_feed(self):
        self.my_profile()
        time.sleep(3)
        self.feed_click_check()
        self.driver.back()
        time.sleep(2)
        self.driver.close()

    def check_privacy_policy(self):
        self.my_profile()
        time.sleep(3)
        self.click_on_privacy_policy()
        time.sleep(1)
        self.driver.close()

    def check_how_it_works(self):
        self.my_profile()
        time.sleep(3)
        self.click_on_how_it_works()
        time.sleep(1)
        self.driver.close()

    def check_terms_of_use(self):
        self.my_profile()
        time.sleep(3)
        self.click_on_terms_of_use()
        time.sleep(1)
        self.driver.close()




