import allure
import urls



class TestPersonalAccount:

    @allure.title("Переход в личный кабинет через кнопку навигации")
    def test_navigate_to_personal_account(self, open_url, personal_acc_page, login_page):
        open_url(personal_acc_page, urls.BASE_URL)
        login_page.login()
        personal_acc_page.click_personal_acc()
        personal_acc_page.assert_redirect_personal_acc()

    @allure.title("Отображение истории заказов")
    def test_display_order_history(self, open_url, personal_acc_page, login_page):
        open_url(personal_acc_page, urls.BASE_URL)
        login_page.login()
        personal_acc_page.click_personal_acc()
        personal_acc_page.click_order_history()
        personal_acc_page.assert_found_lst_is_not_empty()

    @allure.title("Выход из аккаунта")
    def test_user_logout(self, open_url, personal_acc_page, login_page):
        open_url(personal_acc_page, urls.BASE_URL)
        login_page.login()
        personal_acc_page.click_personal_acc()
        personal_acc_page.click_logout()
        personal_acc_page.assert_logout_successfully()