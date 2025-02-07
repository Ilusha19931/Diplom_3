from pages.base_page import BasePage
from locators.login_page_locator import LoginPageLocators
import data

class LoginPage(BasePage):


    def login(self):
        self.click_elem(LoginPageLocators.LOGIN_IN_ACCOUNT)
        self.write_in_field(LoginPageLocators.EMAIL_INPUT, data.email)
        self.write_in_field(LoginPageLocators.PASSWORD_INPUT, data.password)
        self.click_elem(LoginPageLocators.LOGIN_BTN)
        self.assert_url('https://stellarburgers.nomoreparties.site/')