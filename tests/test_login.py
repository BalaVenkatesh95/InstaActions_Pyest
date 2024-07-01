# tests/test_login.py
import pytest
from pages.login_page import LoginPage
from pages.base_page import BasePage

url = "https://www.instagram.com/"

base_page = BasePage(url)
login_page = LoginPage(base_page.driver)
USERNAME = "testuserig2k24"
PASSWORD = "tester@IG2025"

def test_login():
    login_page.login(USERNAME, PASSWORD)
    # Add assertions to verify login success
