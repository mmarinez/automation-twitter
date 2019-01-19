from selenium.webdriver.common.by import By

from src.pageobject.Page import Page
from src.pageobject.pagefactory_support import callable_find_by as find_by


class HomePage(Page):
    button_signup = find_by(how=By.XPATH, using="//a[contains(text(),'Sign Up')]")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def go_to_signup_page(self):
        self.button_signup().click()
