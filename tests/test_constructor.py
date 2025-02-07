import pytest
import allure
import urls

class TestConstructor:

    @pytest.mark.parametrize('tab, url', [('Конструктор', urls.BASE_URL),
                                          ('Лента Заказов', urls.FEED_URL)])
    @allure.title("Навигация через кнопки в navbar")
    def test_navigation_via_navbar_buttons(self, open_url, constructor_page, tab, url):
        open_url(constructor_page, urls.LOGIN_URL)
        constructor_page.assert_redirect_nav_tab(url, tab)

    @allure.title("Открытие и закрытие модального окна ингредиента")
    def test_open_and_close_ingredient_modal(self, open_url, constructor_page):
        open_url(constructor_page, urls.BASE_URL)
        constructor_page.assert_modal_window_details_displayed()
        constructor_page.assert_modal_window_closed()

    @allure.title("Создание заказа авторизованным пользователем")
    def test_create_order_as_authorized_user(self, open_url, constructor_page, login_page):
        open_url(constructor_page, urls.BASE_URL)
        login_page.login()
        constructor_page.click_constructor()
        constructor_page.create_order()