from pages.base_page import BasePage
from pages.login_page import LoginPage
from utils.helpers import wait_for_element, wait_for_element_presence, element_clickable
from selenium.webdriver.common.by import By
from utils.screenshot import take_screenshot
import time

class ActionsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)


    def follow_users(self, usernames):
        self.search_button = "(//a[contains(@class, 'x1i10hfl')])[3]"
        self.search_box = "//input[@placeholder='Search']"
        self.follow_button = "//button[contains(., 'Follow')]"

        # Simulate following users on Instagram
        for username in usernames:
            wait_for_element_presence(self.driver, self.search_button)
            self.click_element(self.search_button)
            wait_for_element_presence(self.driver, self.search_box)
            wait_for_element(self.driver, self.search_box)
            self.enter_text(self.search_box, username)
            self.username_select = f"(//a[contains(@class, 'x1i10hfl') and @href='/{username}/'])[1]"
            wait_for_element_presence(self.driver, self.username_select)
            self.click_element(self.username_select)
            wait_for_element(self.driver, self.follow_button)
            element_clickable(self.driver, self.follow_button)
            self.click_element(self.follow_button)
            time.sleep(10)
            take_screenshot(self.driver)


    def like_by_tags(self, tags, amount=10):
        # Simulate liking posts by tags on Instagram
        for tag in tags:
            self.driver.get(f"https://www.instagram.com/explore/tags/{tag}/")
            for _ in range(amount):
                # Example: Click on like buttons for posts
                like_buttons = self.driver.find_elements(By.XPATH, "//span[@aria-label='Like']")
                for button in like_buttons:
                    button.click()
                    time.sleep(3)  # Optional: Add a delay between likes

    def normal_like(self, target_user):
        self.search_button = "(//a[contains(@class, 'x1i10hfl')])[3]"
        self.search_box = "//input[@placeholder='Search']"
        self.first_post = "(//div[@class='_aagw'])[1]"
        self.like_button = "(//div[contains(@class, 'x1i10hfl') and contains(@class, 'x972fbf')])[17]"

        wait_for_element_presence(self.driver, self.search_button)
        self.click_element(self.search_button)
        wait_for_element(self.driver, self.search_box)
        self.enter_text(self.search_box, target_user)
        self.username_select = f"(//a[contains(@class, 'x1i10hfl') and @href='/{target_user}/'])[1]"
        wait_for_element_presence(self.driver, self.username_select)
        self.click_element(self.username_select)

        wait_for_element(self.driver, self.first_post)
        self.click_element(self.first_post)
        wait_for_element(self.driver, self.like_button)
        element_clickable(self.driver, self.like_button)
        self.click_element(self.like_button)


    def normal_comment(self,target_user, comment_text):
        self.search_button = "(//a[contains(@class, 'x1i10hfl')])[3]"
        self.search_box = "//input[@placeholder='Search']"
        self.comment_button = "(//div[contains(@class, 'x1i10hfl') and contains(@class, 'x972fbf')])[18]"
        self.comment_input_field = "//textarea[@aria-label='Add a comment…']"
        self.post_comment_button = "//div[@role='button' and @tabindex='0' and text()='Post']"

        '''
        wait_for_element_presence(self.driver, self.search_button)
        self.click_element(self.search_button)
        wait_for_element(self.driver, self.search_box)
        self.enter_text(self.search_box, target_user)
        self.username_select = f"//a[@href='/{target_user}/']"
        wait_for_element_presence(self.driver, self.username_select)
        self.click_element(self.username_select)
        '''



        wait_for_element(self.driver, self.comment_button)
        element_clickable(self.driver, self.comment_button)
        self.click_element(self.comment_button)
        wait_for_element(self.driver, self.comment_input_field)
        self.enter_text(self.comment_input_field, comment_text)
        wait_for_element(self.driver, self.comment_input_field)

        wait_for_element(self.driver, self.post_comment_button)
        element_clickable(self.driver, self.post_comment_button)
        self.click_element(self.post_comment_button)
        take_screenshot(self.driver)

    def end_session(self):
        self.shutdown()
