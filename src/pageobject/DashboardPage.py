import os
import time

from selenium.webdriver.common.by import By

from src.pageobject.Page import Page
from src.pageobject.pagefactory_support import callable_find_by as find_by


class DashboardPage(Page):
    input_tweet = find_by(how=By.XPATH, using="//div[@aria-labelledby='tweet-box-home-timeline-label']")
    button_tweet_button = find_by(how=By.XPATH, using="(//button/span[@class='button-text tweeting-text'])[1]")
    input_file_upload = find_by(how=By.XPATH, using="(//input[@name='media_empty'])[1]")
    button_file_upload = find_by(how=By.XPATH, using="(//button[@data-original-title='Add photos or video'])[1]")

    def __init__(self, driver):
        super(DashboardPage, self).__init__(driver)

    def input_type_tweet_text(self):
        self.input_tweet().send_keys("Test automation tweet")
        time.sleep(2)
        self.button_tweet_button().click()
        time.sleep(2)

    def input_image_tweet(self):
        time.sleep(2)
        self.input_tweet().send_keys("Test automation image tweet")
        time.sleep(2)
        self.input_file_upload().send_keys(os.path.abspath(os.path.join('../resources', 'transistor' + '.jpg')))
        time.sleep(2)
        self.button_tweet_button().click()
