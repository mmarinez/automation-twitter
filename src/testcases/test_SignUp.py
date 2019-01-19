import time
import unittest

from selenium import webdriver

from src.pageobject.HomePage import HomePage


class TestTwitter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://twitter.com/?lang=en")

        self.homepage = HomePage(self.driver)

    def test_create_user(self):
        self.homepage.go_to_signup_page()
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
