import time
import unittest

from selenium import webdriver

from src.pageobject.HomePage import HomePage
from src.pageobject.SignupPage import SignupPage


class TestTwitter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://twitter.com")

        self.homepage = HomePage(self.driver)

    def test_create_user(self):
        self.homepage.go_to_signup_page()
        self.signuppage = SignupPage(self.driver)
        self.signuppage.create_twitter_account()
        time.sleep(10)

        if self.signuppage.is_user_account_taken():
            assert True

    def test_login_access(self):
        self.homepage.access_twitter_account()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
