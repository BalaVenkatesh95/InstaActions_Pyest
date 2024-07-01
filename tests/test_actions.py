import pytest
from pages.base_page import BasePage
from pages.actions_page import ActionsPage
from pages.login_page import LoginPage

url = "https://www.instagram.com/"
username = "testuserig2k24"
password = "tester@IG2025"
usernames_to_follow = ["theboystv", "yuvisofficial", "manirathnam_frames"]
tags_to_like = ["nature", "photography"]
target_user = "sunnews"
comment_text = "Nice post!"


base_page = BasePage(url)
login_page = LoginPage(base_page.driver)
actions_page = ActionsPage(base_page.driver)


def test_follow_users():
    login_page.login(username, password)
    actions_page.follow_users(usernames_to_follow)


def test_normal_like():
    actions_page.normal_like(target_user)


def test_normal_comment():
    actions_page.normal_comment(target_user, comment_text)


def test_shutdown():
    actions_page.end_session()
