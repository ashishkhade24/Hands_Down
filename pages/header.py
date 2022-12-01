import time
from page_objects.base import Base

class Header_Section(Base):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def check_my_list(self):
        self.click_on_my_list()

    def check_my_saves(self):
        self.click_on_my_saves()

    def check_feed(self):
        self.click_on_feed()

    def check_notifications(self):
        self.click_on_notifications()

    def check_logout(self):
        self.logout()
