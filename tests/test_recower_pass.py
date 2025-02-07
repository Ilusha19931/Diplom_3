import allure
import urls


class TestRecoverPasswordPage:

    @allure.title("Переход на страницу восстановления пароля при нажатии кнопки")
    def test_navigate_to_recover_password_page(self, open_url, recover_password_page):
        open_url(recover_password_page, urls.LOGIN_URL)
        recover_password_page.click_recover_password()
        recover_password_page.assert_redirect_recover_pass()

    @allure.title("Заполнение почты и переход на страницу ввода нового пароля")
    def test_fill_email_and_navigate_to_reset_password(self, open_url, recover_password_page):
        open_url(recover_password_page, urls.FORGOT_PASS_URL)
        recover_password_page.write_email()
        recover_password_page.assert_redirect_reset_pass()

    @allure.title("Проверка отображения пароля при нажатии кнопки показа")
    def test_toggle_password_visibility(self, open_url, recover_password_page):
        open_url(recover_password_page, urls.FORGOT_PASS_URL)
        recover_password_page.write_email()
        recover_password_page.write_password()
        recover_password_page.assert_password_is_displayed()