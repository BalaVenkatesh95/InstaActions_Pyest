# pages/login_page.py
from pages.base_page import BasePage
from utils.helpers import wait_for_element
from utils.helpers import wait_for_element_presence
from utils.helpers import element_clickable
from utils.screenshot import take_screenshot
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.USERNAME_FIELD = "//input[@name='username']"
        self.PASSWORD_FIELD = "//input[@name='password']"
        self.LOGIN_BUTTON = "//button[@type='submit']"

        wait_for_element(self.driver, self.USERNAME_FIELD)
        wait_for_element_presence(self.driver, self.USERNAME_FIELD)
        self.enter_text(self.USERNAME_FIELD, username)
        wait_for_element(self.driver, self.PASSWORD_FIELD)
        wait_for_element_presence(self.driver, self.PASSWORD_FIELD)
        self.enter_text(self.PASSWORD_FIELD, password)
        wait_for_element(self.driver, self.LOGIN_BUTTON)
        element_clickable(self.driver, self.LOGIN_BUTTON)
        self.click_element(self.LOGIN_BUTTON)
        time.sleep(5)
        take_screenshot(self.driver)

