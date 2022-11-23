from page_objects.base import Base
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Edit_Profile(Base):

    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    edit_button = (By.XPATH,"//button[normalize-space()='Edit Profile']")
    last_name_text = (By.XPATH,"//input[@id='last_name']")
    location = (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[4]/div[3]/div[1]/div[2]/div[2]/div[1]/input[1]")
    options=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/form[1]/div[4]/div[3]/div[1]/div[3]/button[1]")
    category= (By.XPATH,"//input[@id='category']")
    category_select= (By.XPATH,"//p[contains(text(),'Clothing')]")
    save_new_categories= (By.XPATH,"/html[1]/body[1]/div[2]/div[3]/div[1]/div[3]/button[1]")
    bio= (By.XPATH,"//textarea[@id='bio_description']")
    save_edit=(By.XPATH,"//button[normalize-space()='Save Edits']")
    preference=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/p[1]")
    button1=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]")
    button2=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/button[2]")
    button3 = (By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[3]/div[1]/button[3]")
    on_button=(By.XPATH,"//label[@for='comment_preferences']")
    save_changes=(By.XPATH,"//button[normalize-space()='Save Changes']")
    password=(By.XPATH,"//p[normalize-space()='Password']")
    old_password=(By.XPATH,"//input[@name='old_password']")
    new_password=(By.XPATH,"//input[@name='new_password']")
    conf_password=(By.XPATH,"//input[@name='confirm_password']")
    save_new_changes=(By.XPATH,"//button[normalize-space()='Save New Categories!']")

    def edit_last_name(self,lastname):
        self.EF.find_element(self.edit_button).click()
        l_name = self.EF.find_element(self.last_name_text)
        actions = ActionChains(self.driver)
        actions.double_click(l_name).send_keys(Keys.BACKSPACE).send_keys(lastname).perform()
        self.EF.find_element(self.save_edit).click()

    def edit_location(self,city_name):
        self.EF.find_element(self.edit_button).click()
        city = self.EF.find_element(self.location)
        time.sleep(1)
        city.send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        city.send_keys(Keys.DELETE)
        time.sleep(2)
        city.send_keys(city_name)
        time.sleep(2)
        drop_down = self.EF.find_element(self.options)
        time.sleep(2)
        drop_down.click()
        time.sleep(3)
        self.EF.find_element(self.save_edit).click()

    def edit_bio(self,designation):
        self.EF.find_element(self.edit_button).click()
        bio_section = self.EF.find_element(self.bio)
        time.sleep(1)
        bio_section.send_keys(Keys.CONTROL + "a")
        time.sleep(2)
        bio_section.send_keys(Keys.DELETE)
        time.sleep(2)
        bio_section.send_keys(designation)
        time.sleep(1)
        self.EF.find_element(self.save_edit).click()

    def edit_categories(self):

        self.EF.find_element(self.edit_button).click()
        self.EF.find_element(self.category).click()
        time.sleep(1)
        dropdown_element = self.EF.find_element(self.category_select).click()
        self.driver.find_element(By.XPATH,
                                 "//button[contains(text(),'Save New Categories!')]").click()
        actions = ActionChains(self.driver)
        actions.click(on_element=dropdown_element)
        time.sleep(2)
        actions.perform()
        time.sleep(2)
        self.EF.find_element(self.save_edit).click()

    def email_preference(self):
        self.EF.find_element(self.edit_button).click()
        self.EF.find_element(self.preference).click()
        self.EF.find_element(self.button1).click()
        self.EF.find_element(self.button2).click()
        self.EF.find_element(self.button3).click()
        self.EF.find_element(self.on_button).click()
        self.EF.find_element(self.save_changes).click()
        time.sleep(4)

    def password_change(self,old,new,cnfrm):

        self.EF.find_element(self.edit_button).click()
        self.EF.find_element(self.password).click()
        time.sleep(3)
        self.EF.find_element(self.old_password).send_keys(old)
        self.EF.find_element(self.new_password).send_keys(new)
        self.EF.find_element(self.conf_password).send_keys(cnfrm)
        self.EF.find_element(self.save_new_changes).click()





























