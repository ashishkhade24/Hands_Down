from selenium.webdriver.common.by import By
import time
from page_objects.base import Base
from selenium.webdriver.common.keys import Keys

class Search(Base):
    def __init__(self,driver):
        self.driver=driver
        super().__init__(driver)

    search_field=(By.XPATH,"//input[@id='searchInput']")
    people_button=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[2]")
    faves_button=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]")
    cross_button=(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]")
    slide_right=(By.XPATH,"//span[normalize-space()='>']")
    slide_left=(By.XPATH,"//span[normalize-space()='<']")
    add_cart=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[18]/div[1]/div[1]/div[1]/a[1]")
    fit_in=(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/span[19]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/p[1]")
    next_page=(By.XPATH,"//button[normalize-space()='2']")

    def enter_name(self,name):
        search_people=self.EF.find_element(self.search_field)
        search_people.send_keys(name)
        search_people.send_keys(Keys.ENTER)

    def search_people(self,name):
        self.enter_name(name)
        time.sleep(2)
        self.EF.find_element(self.people_button).click()
        time.sleep(2)
        self.EF.find_element(self.faves_button).click()
        time.sleep(2)
        self.driver.save_screenshot("./testdata/screenshot/search_user/search_people_page1.png")
        time.sleep(2)
        self.EF.find_element(self.next_page).click()
        time.sleep(2)
        self.driver.save_screenshot("./testdata/screenshot/search_user/search_people_page2.png")
        self.driver.quit()

    def check_slider(self,name):
        self.enter_name(name)
        time.sleep(2)
        self.EF.find_element(self.slide_right).click()
        time.sleep(3)
        self.EF.find_element(self.slide_left).click()
        time.sleep(3)
        self.driver.quit()

    def check_fave_category(self,name):
        self.enter_name(name)
        time.sleep(2)
        self.EF.find_element(self.fit_in).click()
        time.sleep(2)
        self.driver.save_screenshot("./testdata/screenshot/search_user/category.png")
        time.sleep(2)
        self.driver.back()
        self.driver.quit()

    def check_cart(self,name):
        self.enter_name(name)
        time.sleep(2)
        self.EF.find_element(self.add_cart).click()
        time.sleep(2)
        self.driver.save_screenshot("./testdata/screenshot/search_user/cart1.png")
        time.sleep(2)
        self.driver.back()
        self.driver.quit()












