from selenium.webdriver.common.by import By
from page_objects.base import Base
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Edit_user_list(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    my_list=(By.XPATH,"//p[normalize-space()='My Lists']")
    archive=(By.XPATH,"//p[normalize-space()='Archived']")
    edit_button=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]")
    add_fav_to_list=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/p[1]")
    continue_to_details=(By.XPATH,"//button[normalize-space()='Continue to Details']")
    select_list=(By.XPATH,"/html[1]/body[1]/div[3]/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]")
    publish_button=(By.XPATH,"//button[normalize-space()='Publish']")
    fav_things = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/p[1]")
    list_edit=(By.XPATH,"//button[normalize-space()='List Editor']")
    view_comment = (By.XPATH, "//p[@class='Text__Label-sc-4on308-0 diJbvN']")
    leave_comment=(By.XPATH,"//input[@class='comments-textarea__input']")
    click=(By.XPATH,"//button[@class='Button__StyledButton-sc-bpb489-0 hdHWlJ AddComment__Button-sc-lbet42-2 jJckPI']")
    Edit_link=(By.XPATH,"//*[@id='__next']/div/div[2]/div/div[2]/div[1]/div/div/div[2]")
    edit_fav=(By.XPATH,"//p[normalize-space()='Edit Fave']")
    title_text=(By.NAME,"name")
    select_category = (By.XPATH,"//div[@id='selector-category']")
    category=(By.XPATH,"//li[normalize-space()='Fitness']")
    comment=(By.NAME,"commentary")
    save_changes=(By.XPATH,"//button[normalize-space()='Save Changes']")
    archive_fave=(By.XPATH,"//p[normalize-space()='Archive Fave']")
    archive_fave_save=(By.XPATH,"//button[normalize-space()='Archive Fave']")
    copy_fave=(By.XPATH,"//p[normalize-space()='Copy Fave to another list']")
    location=(By.XPATH,"//body[1]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]")
    copy_save=(By.XPATH,"//button[normalize-space()='Save Changes!']")
    search_text=(By.XPATH,"//input[@placeholder='Search the web or paste a link']")
    wikipedia=(By.XPATH,"//div[normalize-space()='India - Wikipedia']")
    add_fave_category=(By.XPATH,"//div[@id='selector-category']")
    podcast=(By.XPATH,"//li[normalize-space()='Podcasts']")
    add_list=(By.XPATH,"//div[@id='selector-list']")
    list_field=(By.XPATH,"//li[normalize-space()='Books']")
    comment_text=(By.XPATH,"//textarea[@id='outlined-textarea']")
    publish=(By.XPATH,"//button[normalize-space()='Publish']")
    add_another_fave=(By.XPATH,"//button[normalize-space()='Add Another Fave']")
    go_to_list=(By.XPATH,"//button[normalize-space()='Go To List']")
    Book_read=(By.XPATH,"//p[normalize-space()='Books_read']")
    add_fave=(By.XPATH,"//button[normalize-space()='Add New Fave!']")
    all_buttons = (By.XPATH, "/html[1]/body[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div[1]/div")
    Add_New_Fave = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[2]")
    button_link=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]")
    preview_list=(By.XPATH,"(//p[normalize-space()='Preview List'])[1]")
    back_button=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]")
    share_to=(By.XPATH,"//p[normalize-space()='Share to']")
    all_elements=(By.XPATH,"/html[1]/body[1]/div[2]/div[3]/div[1]/div[3]/div[1]/div[1]/div")

    def edit_fave(self,name,details):
        time.sleep(3)
        self.EF.find_element(self.Edit_link).click()
        time.sleep(5)
        self.EF.find_element(self.edit_fav).click()
        title_name=self.EF.find_element(self.title_text)
        time.sleep(1)
        title_name.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        title_name.send_keys(Keys.DELETE)
        time.sleep(1)
        title_name.send_keys(name)
        time.sleep(1)
        self.EF.find_element(self.select_category).click()
        self.EF.find_element(self.category).click()
        recommendation=self.EF.find_element(self.comment)
        recommendation.send_keys(Keys.CONTROL + "a")
        time.sleep(1)
        recommendation.send_keys(Keys.DELETE)
        time.sleep(1)
        recommendation.send_keys(details)
        self.EF.find_element(self.save_changes).click()

    def copy_a_fave(self):
        time.sleep(3)
        self.EF.find_element(self.Edit_link).click()
        time.sleep(5)
        self.EF.find_element(self.copy_fave).click()
        self.EF.find_element(self.location).click()
        self.EF.find_element(self.copy_save).click()

    def click_archive(self):
        time.sleep(3)
        self.EF.find_element(self.Edit_link).click()
        time.sleep(5)
        self.EF.find_element(self.archive_fave).click()
        time.sleep(3)
        self.EF.find_element(self.archive_fave_save).click()
        time.sleep(3)

    def restore_fave(self):
        self.EF.find_element(self.my_list).click()
        self.EF.find_element(self.archive).click()
        self.EF.find_element(self.edit_button).click()
        self.EF.find_element(self.add_fav_to_list).click()
        self.EF.find_element(self.continue_to_details).click()
        actions=ActionChains(self.driver)
        list=self.EF.find_element(self.select_list)
        actions.click(list).perform()
        self.EF.find_element(self.publish_button).click()
        self.EF.find_element(self.go_to_list).click()

    def click_comment(self,comment):
        self.EF.find_element(self.view_comment).click()
        self.EF.find_element(self.leave_comment).send_keys(comment)
        self.EF.find_element(self.click).click()
        self.driver.quit()

    def add_a_new_fav(self,search,text):
        time.sleep(3)
        self.EF.find_element(self.Add_New_Fave).click()
        time.sleep(3)
        search_things=self.EF.find_element(self.search_text)
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
        time.sleep(2)
        # self.EF.find_element(self.go_to_list).click()
        # time.sleep(2)
        self.driver.quit()

    def share_list(self):
        time.sleep(3)
        buttons = self.EF.find_elements(self.all_buttons)
        for button in buttons:
            button.click()
            time.sleep(1)
        self.driver.back()
        time.sleep(1)
        # self.driver.quit()

    def click_preview_list_and_share_to(self):

        self.EF.find_element(self.button_link).click()
        time.sleep(2)
        self.EF.find_element(self.preview_list).click()
        time.sleep(2)
        self.EF.find_element(self.back_button).click()
        time.sleep(1)
        self.driver.refresh()
        time.sleep(1)
        self.EF.find_element(self.button_link).click()
        time.sleep(1)
        self.EF.find_element(self.share_to).click()
        time.sleep(1)
        buttons = self.EF.find_elements(self.all_elements)
        for button in buttons:
            button.click()
            time.sleep(1)

    def add_fave_in_new_list(self,search,text):
        time.sleep(3)
        self.EF.find_element(self.add_fave).click()
        time.sleep(3)
        element=self.EF.find_element(self.search_text)
        element.send_keys(search)
        element.send_keys(Keys.ENTER)
        self.EF.find_element(self.wikipedia).click()
        self.EF.find_element(self.add_fave_category).click()
        self.EF.find_element(self.podcast).click()
        self.EF.find_element(self.add_list).click()
        self.EF.find_element(self.list_field).click()
        self.EF.find_element(self.comment_text).send_keys(text)
        self.EF.find_element(self.publish).click()
        self.EF.find_element(self.go_to_list).click()
        self.driver.quit()






































