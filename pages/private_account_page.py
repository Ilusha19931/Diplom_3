import urls
from pages.base_page import BasePage
import allure
from locators.private_account_locator import PrivateAccountLocators


class PryvateAccountPage(BasePage):

    @allure.step("Клик по ЛК")
    def click_personal_acc(self):
        self.click_elem(PrivateAccountLocators.PERSONAL_ACCOUNT)

    @allure.step("Клик по Истории заказов")
    def click_order_history(self):
        self.click_elem(PrivateAccountLocators.ORDER_HISTORY)

    @allure.step("Клик по лого")
    def click_logo(self):
        self.click_elem(PrivateAccountLocators.STELLAR_LOGO)

    @allure.step("Клик по кнопке выход")
    def click_logout(self):
        self.click_elem(PrivateAccountLocators.LOGOUT_BTN)

    @allure.step("Список заказов, формирование")
    def return_order_list(self):
        lst = self.find_elements(PrivateAccountLocators.ORDERS_LST)
        return len(lst)

    @allure.step("Переход к последнему элементу списка заказов")
    def scroll_to_last_order(self):
        scrollable_lst = self.find_element(PrivateAccountLocators.ORDER_LIST)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_lst)

    @allure.step("Список заказов не пустой")
    def assert_found_lst_is_not_empty(self):
        assert self.return_order_list() != 0

    @allure.step("Выход из аккаунта")
    def assert_logout_successfully(self):
        self.assert_url(urls.LOGIN_URL)
        assert self.find_element(PrivateAccountLocators.LOGIN_ACC).is_displayed() == True

    @allure.step("Проверка перехода на профиль")
    def assert_redirect_personal_acc(self):
        self.assert_redirect_page(urls.PROFILE_URL, PrivateAccountLocators.PROFILE_PAGE_DESCRIPTION)