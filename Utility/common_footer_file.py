from selenium.webdriver.common.by import By
from page_objects.base import Base
import time

class Footer_Page_Check(Base):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    logo_click = (By.XPATH, "//img[contains(@class,'Branding__Image-sc-1earmyc-0 JoXpk')]")
    feed_click = (By.LINK_TEXT, "Feed")
    privacy_policy = (By.LINK_TEXT, "Privacy Policy")
    how_it_works = (By.LINK_TEXT, "How It Works")
    terms_of_use = (By.LINK_TEXT, "Terms Of Use")
    explore= (By.XPATH,"//a[normalize-space()='Explore']")
    header_tabs=(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[2]/div[1]/ul[1]/li")
    login_button=(By.XPATH,"//div[@class='redirect']//a[normalize-space()='Login']")
    join_now_button=(By.XPATH,"//div[@class='block']//a[@class='btn'][normalize-space()='Join Now!']")
    social_links= (By.XPATH,"//div[@class='Footer__SocialMediaItemContainer-sc-h6qgl6-2 NkWtV']")
    social_link_footer = (By.XPATH, "/html[1]/body[1]/div[1]/footer[1]/div[1]/div[1]/div[2]/div[2]/div")
    join_now_link=(By.XPATH,"//a[normalize-space()='Join Now']")
    login_link=(By.XPATH,"/html[1]/body[1]/div[1]/footer[1]/div[1]/div[1]/div[3]/ul[1]/li[5]/a[1]")
    your_name=(By.XPATH,"/html[1]/body[1]/div[1]/footer[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[1]/div[1]/input[1]")
    email_add=(By.XPATH,"/html[1]/body[1]/div[1]/footer[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[2]/div[1]/input[1]")
    text_area=(By.XPATH,"/html[1]/body[1]/div[1]/footer[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[3]/div[1]/textarea[1]")
    submit_button =(By.XPATH,"/html[1]/body[1]/div[1]/footer[1]/div[1]/div[1]/div[4]/div[1]/form[1]/div[4]/div[2]/input[1]")
    footer_logo=(By.XPATH,"/html[1]/body[1]/div[1]/footer[1]/div[1]/div[1]/div[2]/div[1]/a[1]/img[1]")
    home=(By.XPATH,"//a[normalize-space()='Home']")
    how_it_work_tab=(By.XPATH,"/html[1]/body[1]/div[1]/header[1]/nav[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/a[1]")
    the_high_five=(By.LINK_TEXT,"The High Five")

    def click_on_footer_logo(self):
        self.EF.find_element(self.logo_click)

    def click_on_social_link(self):
        self.EF.find_elements(self.social_links).click()

    def feed_click_check(self):
        self.EF.find_element(self.feed_click).click()

    def click_on_privacy_policy(self):
        self.EF.find_element(self.privacy_policy).click()

    def click_on_how_it_works(self):
        self.EF.find_element(self.how_it_works).click()

    def click_on_terms_of_use(self):
        self.EF.find_element(self.terms_of_use).click()

    def click_on_logo_and_social_link(self):
        self.click_on_footer_logo()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        links= self.EF.find_elements(self.social_links)
        for link in links:
            link.click()
            time.sleep(2)
        self.driver.back()
        self.driver.quit()

    def click_on_header_tabs(self):
        self.EF.find_element(self.home).click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.EF.find_element(self.how_it_work_tab).click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)
        self.EF.find_element(self.the_high_five).click()
        time.sleep(2)
        self.driver.back()

    def click_on_login_button(self):
        self.EF.find_element(self.login_button).click()
        time.sleep(2)
        self.driver.back()

    def click_on_join_now_button(self):
        self.EF.find_element(self.join_now_button).click()
        time.sleep(2)
        self.driver.back()

    def footer_logo_and_links(self):
        self.EF.find_element(self.footer_logo).click()
        time.sleep(3)
        self.driver.back()
        links=self.EF.find_element(self.social_link_footer)
        for link in links:
            link.click()
            time.sleep(1)

    def click_footer_links(self):
        self.click_on_privacy_policy()
        time.sleep(3)
        self.click_on_how_it_works()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.click_on_terms_of_use()
        time.sleep(3)
        self.EF.find_element(self.explore).click()
        time.sleep(3)
        self.driver.back()
        self.EF.find_element(self.login_link).click()
        time.sleep(3)
        self.driver.back()
        time.sleep(3)
        self.EF.find_element(self.join_now_link).click()
        time.sleep(3)
        self.driver.back()

    def contact_us(self,name,email,message):
        full_name=self.EF.find_element(self.your_name)
        full_name.clear()
        full_name.send_keys(name)
        time.sleep(2)
        email_details=self.EF.find_element(self.email_add)
        email_details.clear()
        email_details.send_keys(email)
        time.sleep(2)
        text=self.EF.find_element(self.text_area)
        text.clear()
        text.send_keys(message)
        email_details.send_keys(email)
        time.sleep(2)
        self.EF.find_element(self.submit_button).click()




