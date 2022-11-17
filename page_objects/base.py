from selenium.webdriver.common.by import By
from Utility.elementry_function import Elem_fun

class Base:

    def __init__(self,driver):
        self.driver = driver
        self.EF = Elem_fun(self.driver)

    drop_down=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]")
    profile=(By.XPATH,"//p[normalize-space()='My Profile']")
    logout_button=(By.XPATH,"//p[normalize-space()='Logout']")

    def click_on_drop_down(self):
        self.EF.find_element(self.drop_down).click()

    def click_on_my_profile(self):
        self.EF.find_element(self.profile).click()

    def click_on_logout(self):
        self.EF.find_element(self.logout_button).click()

    def logout(self):
        self.click_on_logout()
        self.logout()

    def navigate_to_tab(self,tab):
        self.EF.find_element(tab)






