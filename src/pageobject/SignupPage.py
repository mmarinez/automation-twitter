import time

from selenium.webdriver.common.by import By

from src.pageobject.Page import Page
from src.pageobject.pagefactory_support import callable_find_by as find_by
from src.values import config


class SignupPage(Page):
    input_user_real_name = find_by(how=By.XPATH, using="//input[starts-with(@placeholder,'Name')]")
    input_user_email = find_by(how=By.XPATH, using="//input[starts-with(@placeholder,'Email')]")
    hyperlink_change_to_email = find_by(how=By.XPATH, using="//div[contains(text(),'email')]")
    button_next = find_by(how=By.XPATH, using="//span[contains(text(),'Next')]")
    button_signUp = find_by(how=By.XPATH, using="//div[contains(@role,'button')]/div/span[text()='Sign up']")
    text_error_message = find_by(how=By.XPATH, using="//div[contains(text(),'Email has already been taken.')]")

    def __init__(self, driver):
        super(SignupPage, self).__init__(driver)

    def create_twitter_account(self):
        self.input_user_real_name().send_keys(config.user_name)
        self.hyperlink_change_to_email().click()
        self.input_user_email().send_keys(config.email)
        time.sleep(2)
        self.button_next().click()
        time.sleep(2)
        self.button_signUp().click()

    def is_user_account_taken(self):
        return self.text_error_message().is_displayed()
