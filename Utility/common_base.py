from selenium.webdriver.common.by import By
import time
from page_objects.base import Base
from pages.edit_profile import Edit_Profile
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Base_Features(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)
        self.EP=Edit_Profile(self.driver)

    followers = (By.XPATH, "//p[normalize-space()='Follower']")
    following = (By.XPATH, "//p[normalize-space()='Following']")
    back_button_follower = (By.XPATH, "//h1[contains(@class,'Text__H1-sc-4on308-1 fqthkj')]")
    back_button_following = (By.XPATH, "//h1[contains(@class,'Text__H1-sc-4on308-1 fqthkj')]")
    find_someone = (By.XPATH, "//input[@placeholder='Find someone']")
    all_followers = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div")
    user_click = (By.XPATH, "//p[normalize-space()='Mahesh Soni']")
    unfollow = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[9]/button[1]")
    view_more = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[2]/p[1]")
    saves = (By.XPATH, "//p[normalize-space()='Saves']")
    explore_feed=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/button[1]")
    archive = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/ul[1]/li[3]/p[1]")
    create_list = (By.XPATH, "//button[normalize-space()='+ Create New List!']")
    input_list_field = (By.XPATH, "//input[contains(@name,'list_name')]")
    select_category = (By.XPATH, "//div[@id='selector-category_id']")
    category = (By.XPATH, "//li[normalize-space()='Books']")
    save_list = (By.XPATH, "//button[normalize-space()='Save & Create List']")
    view_list=(By.XPATH,"//button[normalize-space()='View List']")
    invite_friend = (By.XPATH, "//button[normalize-space()='Invite Friends to HandsDown!']")
    enter_email = (By.XPATH, "//input[@id='downshift-multiple-input']")
    send_invite = (By.XPATH, "//button[normalize-space()='Send Invite!']")
    close_button = (By.XPATH, "//button[normalize-space()='Close & Explore More!']")
    edit_button = (By.XPATH, "//button[normalize-space()='Edit Profile']")
    save_edit = (By.XPATH, "//button[normalize-space()='Save Edits']")
    share_profile = (By.XPATH, "//div[@class='ShareButton__ShareRect-sc-wu3abh-0 enGUFF']")
    all_buttons = (By.XPATH, "/html[1]/body[1]/div[3]/div[3]/div[1]/div[3]/div[1]/div[1]/div")
    back_arrow = (By.XPATH, "/html[1]/body[1]/div[3]/div[3]/div[1]/div[2]")
    copy_link = (By.XPATH, "//div[@class='ShareLinkModal__LinkIconContainer-sc-hz3l3p-2 ggaYCK']")
    add_fave=(By.XPATH,"/html[1]/body[1]/div[3]/div[3]/div[1]/div[2]/button[2]")
    search_text = (By.XPATH, "//input[@placeholder='Search the web or paste a link']")
    wikipedia = (By.XPATH, "//div[normalize-space()='India - Wikipedia']")
    add_fave_category = (By.XPATH, "//div[@id='selector-category']")
    podcast = (By.XPATH, "//li[normalize-space()='Podcasts']")
    add_list = (By.XPATH, "//div[@id='selector-list']")
    list_field = (By.XPATH, "//li[normalize-space()='Books']")
    comment_text = (By.XPATH, "//textarea[@id='outlined-textarea']")
    publish = (By.XPATH, "//button[normalize-space()='Publish']")
    add_another_fave = (By.XPATH, "//button[normalize-space()='Add Another Fave']")
    go_to_list = (By.XPATH, "//button[normalize-space()='Go To List']")

    def share_link(self):
        self.EF.find_element(self.share_profile).click()
        buttons = self.EF.find_elements(self.all_buttons)
        for button in buttons:
            button.click()
            time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.quit()

    def copy_the_link(self):
        self.EF.find_element(self.share_profile).click()
        self.EF.find_element(self.copy_link).click()
        self.EF.find_element(self.back_arrow).click()

    def back_arrow_check(self):
        self.EF.find_element(self.share_profile).click()
        self.EF.find_element(self.back_arrow).click()
        self.driver.quit()

    def followers_section(self, name):
        self.EF.find_element(self.followers).click()
        self.EF.find_element(self.find_someone).send_keys(name)
        time.sleep(2)
        self.EF.find_element(self.back_button_follower).click()
        self.driver.quit()

    def following_section(self, name):
        self.EF.find_element(self.following).click()
        self.EF.find_element(self.find_someone).send_keys(name)
        time.sleep(2)
        self.driver.refresh()
        self.EF.find_element(self.view_more).click()
        time.sleep(2)
        self.EF.find_element(self.user_click).click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.EF.find_element(self.unfollow).click()
        time.sleep(3)
        self.EF.find_element(self.back_button_following).click()
        self.driver.quit()

    def check_edit_profile(self,first_name,lastname,city_name,designation):
        self.EP.edit_first_name(first_name)
        self.EP.edit_last_name(lastname)
        self.EP.edit_location(city_name)
        self.EP.edit_bio(designation)
        self.EP.edit_categories()
        self.EP.save_edit()

    def click_saves_archive(self):
        self.EF.find_element(self.archive).click()
        time.sleep(3)
        self.EF.find_element(self.saves).click()
        time.sleep(3)
        self.EF.find_element(self.explore_feed).click()
        time.sleep(3)
        self.driver.quit()

    def create_new_list(self,list_name):
        self.EF.find_element(self.create_list).click()
        time.sleep(1)
        input_text = self.EF.find_element(self.input_list_field)
        time.sleep(1)
        input_text.clear()
        input_text.send_keys(list_name)
        self.EF.find_element(self.select_category).click()
        self.EF.find_element(self.category).click()
        self.EF.find_element(self.save_list).click()
        time.sleep(2)

    def create_list_and_add_fave(self,list_name,search,text):
        self.create_new_list(list_name)
        time.sleep(3)
        self.EF.find_element(self.add_fave).click()
        time.sleep(3)
        search_things = self.EF.find_element(self.search_text)
        search_things.clear()
        search_things.send_keys(search)
        search_things.send_keys(Keys.ENTER)
        self.EF.find_element(self.wikipedia).click()
        self.EF.find_element(self.add_fave_category).click()
        self.EF.find_element(self.podcast).click()
        self.EF.find_element(self.add_list).click()
        self.EF.find_element(self.list_field).click()
        self.EF.find_element(self.comment_text).send_keys(text)
        self.EF.find_element(self.publish).click()
        self.EF.find_element(self.go_to_list).click()
        self.driver.quit()

    def invite_a_friend(self,email):
        self.EF.find_element(self.invite_friend).click()
        self.EF.find_element(self.enter_email).send_keys(email)
        click_button=self.EF.find_element(self.send_invite)
        print(click_button.is_enabled())
        click_button.click()
        self.EF.find_element(self.close_button).click()
        self.driver.quit()






