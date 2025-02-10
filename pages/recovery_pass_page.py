import urls
import data
import allure
from locators.recovery_locators import RecoveryLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class RecoverPasswordPage(BasePage):

    @allure.step("Клик по кнопке восстановить пароль")
    def click_recover_password(self):
        self.click_elem(RecoveryLocators.RECOVER_PASS_BTN)

    @allure.step("Ввод имейла в поле")
    def write_email(self):
        self.write_in_field(RecoveryLocators.EMAIL_INPUT, data.email)
        self.find_element(RecoveryLocators.RESTORE_BNT).click()

    @allure.step("Ввод пароля в поле")
    def write_password(self):
        self.write_in_field(RecoveryLocators.PASSWORD_INPUT, data.password)


    @allure.step("Работа кнопки показа пароля")
    def assert_password_is_displayed(self):
        self.click_elem(RecoveryLocators.SHOW_PASS_BTN)
        attribute = self.find_element(RecoveryLocators.SHOW_PASS_BTN_CHANGE_TYPE, condition=EC.visibility_of_element_located)
        assert attribute != None

    @allure.step("Проверка перехода восстановления пароля")
    def assert_redirect_recover_pass(self):
        self.assert_redirect_page(urls.FORGOT_PASS_URL, RecoveryLocators.RECOVER_PASS_TITTLE)

    @allure.step("Проверка перехода изменения пароля")
    def assert_redirect_reset_pass(self):
        self.assert_redirect_page(urls.RESET_PASS_URL, RecoveryLocators.PASSWORD_INPUT)