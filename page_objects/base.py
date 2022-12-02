from selenium.webdriver.common.by import By
from Utility.elementry_function import Elem_fun

class Base:

    def __init__(self,driver):
        self.driver = driver
        self.EF = Elem_fun(self.driver)

    drop_down=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]")
    profile=(By.XPATH,"//p[normalize-space()='My Profile']")
    logout_button=(By.XPATH,"//p[normalize-space()='Logout']")
    Feed=(By.XPATH,"//p[normalize-space()='Feed']")
    my_list=(By.XPATH,"//p[normalize-space()='My Lists']")
    my_saves=(By.XPATH,"//p[normalize-space()='My Saves']")
    notifications=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/*[name()='svg'][1]")
    click_name = (By.XPATH, "//p[contains(@class,'Text__Label-sc-4on308-0 hFVtCX ProfileBox__Name-sc-nb8ud1-1 gKHSWS')]")
    edit_button = (By.XPATH, "//button[normalize-space()='Edit Profile']")
    logo=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/img[1]")

    def click_on_drop_down(self):
        self.EF.find_element(self.drop_down).click()

    def click_on_my_profile(self):
        self.EF.find_element(self.profile).click()

    def click_on_feed(self):
        self.EF.find_element(self.Feed).click()

    def click_on_my_list(self):
        self.EF.find_element(self.my_list).click()

    def click_on_my_saves(self):
        self.EF.find_element(self.my_saves).click()

    def click_on_notifications(self):
        self.EF.find_element(self.notifications).click()

    def click_on_name(self):
        self.EF.find_element(self.click_name).click()

    def edit_profile_button(self):
        self.EF.find_element(self.edit_button).click()

    def click_on_logout(self):
        self.EF.find_element(self.logout_button).click()

    def click_on_logo(self):
        self.EF.find_element(self.logo).click()

    def logout(self):
        self.click_on_drop_down()
        self.click_on_logout()








