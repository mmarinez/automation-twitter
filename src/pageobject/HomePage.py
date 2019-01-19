import time

from selenium.webdriver.common.by import By

from src.pageobject.Page import Page
from src.pageobject.pagefactory_support import callable_find_by as find_by
from src.values import config


class HomePage(Page):
    button_signup = find_by(how=By.XPATH, using="//a[contains(text(),'Sign Up')]")
    input_email = find_by(how=By.XPATH, using="//input[@placeholder='Phone, email or username']")
    input_password = find_by(how=By.XPATH, using="//input[@name='session[password]' and starts-with(@class,'js')]")
    button_login = find_by(how=By.XPATH, using="(//button[text()='Log in'])")
    button_login_home = find_by(how=By.XPATH, using="//a[contains(text(),'Log in') and starts-with(@class,'js')]")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def go_to_signup_page(self):
        self.button_signup().click()

    def access_twitter_account(self):
        self.button_login_home().click()
        time.sleep(2)
        self.input_email().send_keys(config.email)
        self.input_password().send_keys(config.password)
        self.button_login().click()
