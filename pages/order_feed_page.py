from locators.order_feed_locator import OrdersFeedLocators
from pages.base_page import BasePage
import allure
from locators.constructor_locator import ConstructorLocators
from locators.private_account_locator import PrivateAccountLocators

class OrdersFeedPage(BasePage):

    id = ''
    initial_count_all_times = ''
    initial_count_today = ''

    @allure.step("Клик по первому заказу")
    def open_first_order(self):
        self.find_element(OrdersFeedLocators.FIRST_ORDER_ID).click()

    @allure.step("ИД заказа")
    def return_order_id(self):
        self.waiting_change_value(ConstructorLocators.ORDER_ID, '9999')
        self.id = self.return_text(ConstructorLocators.ORDER_ID)
        return self.id

    @allure.step("ИД заказа в работе")
    def return_order_in_work(self):
        self.waiting_change_value(OrdersFeedLocators.ORDER_IN_WORKS, 'Все текущие заказы готовы!', 30)
        order_id = self.return_text(OrdersFeedLocators.ORDER_IN_WORKS)
        return order_id

    @allure.step("Заказы за сегодня вывод")
    def return_current_count_today(self):
        self.initial_count_today = self.return_text(OrdersFeedLocators.COUNT_TODAY)
        return self.initial_count_today

    @allure.step("Заказы за все время")
    def return_current_count_all_time(self):
        self.initial_count_all_times = self.return_text(OrdersFeedLocators.COUNT_ALL_TIMES)
        return self.initial_count_all_times

    @allure.step("Cозданный заказ в ленте заказов")
    def assert_created_order_has_in_tape(self):
        first_order_id = self.return_text(OrdersFeedLocators.ORDER_ID)
        assert f'#0{self.id}' == first_order_id, f'#{self.id} != {first_order_id}'

    @allure.step("Cозданный заказ появился в истории заказов")
    def assert_created_order_has_in_order_history(self):
        last_order_id = ''
        list_elem = self.find_elements(PrivateAccountLocators.ORDERS_ID_IN_HISTORY)
        if list_elem:
            last_order_id = list_elem[-1].text
            return last_order_id
        assert f'#0{self.id}' == last_order_id, f'#0{self.id} != {last_order_id}'

    @allure.step("Cозданный заказ появился в разделе 'В работе'")
    def assert_created_order_has_in_work(self):
        assert f'{self.id}' == self.return_order_in_work(), f'0{self.id} != {self.return_order_in_work()}'

    @allure.step("Модальное окно с описанием заказа открыто")
    def assert_modal_window_order_displayed(self):
        assert self.return_text(OrdersFeedLocators.COMPOUND_TITLE) == 'Cостав'

    @allure.step("Счетчик заказов изменился")
    def assert_increment_count(self):
        current_count_all_times = self.return_text(OrdersFeedLocators.COUNT_ALL_TIMES)
        current_count_today = self.return_text(OrdersFeedLocators.COUNT_TODAY)
        assert (int(self.initial_count_today) < int(current_count_today)) and (int(self.initial_count_all_times) < int(current_count_all_times)),\
        f'{self.initial_count_today} !< {current_count_today}, {self.initial_count_all_times} !< {current_count_all_times})'