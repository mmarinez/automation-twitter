import time
import unittest

from selenium import webdriver

from src.pageobject.DashboardPage import DashboardPage
from src.pageobject.HomePage import HomePage
from src.pageobject.SignupPage import SignupPage


class Twitter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://twitter.com")

        self.homepage = HomePage(self.driver)
        self.dashboardpage = DashboardPage(self.driver)

    def test_create_user(self):
        self.homepage.go_to_signup_page()
        self.signuppage = SignupPage(self.driver)
        self.signuppage.create_twitter_account()
        time.sleep(10)

        if self.signuppage.is_user_account_taken():
            assert True

    def test_text_tweet(self):
        self.homepage.access_twitter_account()
        self.dashboardpage.input_type_tweet_text()

    def test_text_link_tweet(self):
        self.homepage.access_twitter_account()
        self.dashboardpage.input_type_tweet_link()

    def test_image_text_tweet(self):
        self.homepage.access_twitter_account()
        self.dashboardpage.input_image_tweet()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
