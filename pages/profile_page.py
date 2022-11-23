from selenium.webdriver.common.by import By
from page_objects.base import Base
import time

class Profile(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    click_name= (By.XPATH,"//p[contains(@class,'Text__Label-sc-4on308-0 hFVtCX ProfileBox__Name-sc-nb8ud1-1 gKHSWS')]")
    invite_friend=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/button[1]")
    input_field=(By.XPATH,"//input[@id='downshift-multiple-input']")
    send_invite=(By.XPATH,"//button[normalize-space()='Send Invite!']")
    copy_link=(By.XPATH,"//p[contains(@class,'Text__Label-sc-4on308-0 bFklBi')]")
    close_button=(By.XPATH,"//button[normalize-space()='Close & Explore More!']")
    followers=(By.XPATH,"//p[normalize-space()='Followers']")
    find_someone=(By.XPATH,"//input[@placeholder='Find someone']")
    following=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[2]/div[3]")
    click_following=(By.XPATH,"//p[normalize-space()='Ayushi ayu Ayushi gothi']")
    saves=(By.XPATH,"//p[@class='Text__Label-sc-4on308-0 gWFsKG TabsNav__Title-sc-1mllghx-3 cXvJLw']")
    archive=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[3]/p[1]")
    create_list=(By.XPATH,"//button[normalize-space()='+ Create New List!']")
    input_list_field=(By.XPATH,"//input[contains(@name,'list_name')]")
    select_category=(By.XPATH,"//div[@id='selector-category_id']")
    list_box=(By.XPATH,"//ul[@role='listbox']")
    category=(By.XPATH,"//li[normalize-space()='Art']")
    save_list=(By.XPATH,"//button[normalize-space()='Save & Create List']")

    def invite_a_friend(self,name):
        self.EF.find_element(self.click_name).click()
        self.EF.find_element(self.invite_friend).click()
        self.EF.find_element(self.input_field).send_keys(name)
        self.EF.find_element(self.send_invite).is_enabled()
        self.driver.save_screenshot("./testdata/screenshot/profile_page/enabled1.png")
        self.EF.find_element(self.send_invite).click()
        self.driver.save_screenshot("./testdata/screenshot/profile_page/invite1.png")
        self.EF.find_element(self.close_button).click()
        self.driver.quit()

    def invite_a_friend_invalid_id(self,name):
        self.EF.find_element(self.click_name).click()
        self.EF.find_element(self.invite_friend).click()
        self.EF.find_element(self.input_field).send_keys(name)
        self.EF.find_element(self.send_invite).is_enabled()
        self.driver.save_screenshot("./testdata/screenshot/profile_page/not_enabled.png")

    def check_follower(self,name):
        self.EF.find_element(self.click_name).click()
        self.EF.find_element(self.followers).click()
        self.EF.find_element(self.find_someone).send_keys(name)
        time.sleep(3)
        self.driver.save_screenshot("./testdata/screenshot/profile_page/follower_check.png")
        time.sleep(3)
        print("123")
        self.driver.quit()

    def check_following(self):
        self.EF.find_element(self.click_name).click()
        self.EF.find_element(self.following).click()
        self.EF.find_element(self.find_someone).click()
        self.driver.refresh()
        self.EF.find_element(self.click_following).click()
        self.driver.save_screenshot("./testdata/screenshot/profile_page/following_user.png")
        self.driver.quit()

    def click_saves_archive(self):
        self.EF.find_element(self.click_name).click()
        self.EF.find_element(self.saves).click()
        time.sleep(2)
        self.driver.save_screenshot("./testdata/screenshot/profile_page/saves.png")
        time.sleep(2)
        self.EF.find_element(self.archive).click()
        time.sleep(2)
        self.driver.save_screenshot("./testdata/screenshot/profile_page/Archive.png")
        time.sleep(2)
        self.driver.quit()

    def create_new_list(self):
        self.EF.find_element(self.click_name).click()
        time.sleep(1)
        self.EF.find_element(self.create_list).click()
        time.sleep(1)
        input_text = self.EF.find_element(self.input_list_field)
        time.sleep(1)
        input_text.clear()
        input_text.send_keys("art")
        self.EF.find_element(self.select_category).click()
        self.EF.find_element(self.category).click()
        self.EF.find_element(self.save_list).click()
        time.sleep(2)
        self.driver.save_screenshot("./testdata/screenshot/profile_page/list_created.png")
        self.driver.quit()


























