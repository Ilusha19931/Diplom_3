import pytest
import allure
import urls

class TestTapeOrder:

    @pytest.mark.order(2)
    @allure.title("Открытие и закрытие модального окна заказа")
    def test_open_and_close_order_modal_window(self, open_url, tape_orders_page, login_page, constructor_page):
        open_url(tape_orders_page, urls.BASE_URL)
        login_page.login()
        constructor_page.click_tape_orders()
        tape_orders_page.open_first_order()
        tape_orders_page.assert_modal_window_order_displayed()
        constructor_page.assert_modal_window_closed()

    @pytest.mark.order(3)
    @allure.title("Отображение заказов пользователя в ленте заказов и истории заказов")
    def test_user_orders_in_feed_and_history(self, open_url, tape_orders_page, login_page, constructor_page, personal_acc_page):
        open_url(tape_orders_page, urls.BASE_URL)
        login_page.login()
        constructor_page.click_constructor()
        constructor_page.create_order()
        tape_orders_page.return_order_id()
        constructor_page.close_modal_window()
        constructor_page.click_tape_orders()
        tape_orders_page.assert_created_order_has_in_tape()
        personal_acc_page.click_personal_acc()
        personal_acc_page.click_order_history()
        personal_acc_page.scroll_to_last_order()
        tape_orders_page.assert_created_order_has_in_order_history()

    @pytest.mark.order(4)
    @allure.title("Обновление счётчиков выполненных заказов")
    def test_order_counters_increment(self, open_url, tape_orders_page, login_page, constructor_page):
        open_url(tape_orders_page, urls.BASE_URL)
        login_page.login()
        constructor_page.click_tape_orders()
        tape_orders_page.return_current_count_today()
        tape_orders_page.return_current_count_all_time()
        constructor_page.click_constructor()
        constructor_page.create_order()
        constructor_page.click_tape_orders()
        tape_orders_page.assert_increment_count()

    @pytest.mark.order(1)
    @allure.title("Отображение созданного заказа в работе")
    def test_created_order_displayed_as_in_progress(self, open_url, tape_orders_page, login_page, constructor_page):
        open_url(tape_orders_page, urls.BASE_URL)
        login_page.login()
        constructor_page.click_constructor()
        constructor_page.create_order()
        tape_orders_page.return_order_id()
        constructor_page.close_modal_window()
        constructor_page.click_tape_orders()
        tape_orders_page.return_order_in_work()
        tape_orders_page.assert_created_order_has_in_work()