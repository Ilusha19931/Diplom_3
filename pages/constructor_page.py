from pages.base_page import BasePage
import allure
from locators.constructor_locator import ConstructorLocators


class ConstructorPage(BasePage):
    @allure.step("Клик по кнопке конструктор")
    def click_constructor(self):
        self.click_elem(ConstructorLocators.CONSTRUCTOR_BTN)

    @allure.step("Клик по кнопке заказ")
    def click_tape_orders(self):
        self.click_elem(ConstructorLocators.ORDERS_TAPE_BTN)

    @allure.step("Клик по кнопке ингра")
    def click_to_bun(self):
        self.find_element(ConstructorLocators.BUNS).click()

    @allure.step("Клик по кнопке заказать")
    def click_create_order(self):
        self.click_elem(ConstructorLocators.CREATE_ORDER_BTN)
        assert self.return_text(ConstructorLocators.ORDER_STATUS) == 'Ваш заказ начали готовить'

    @allure.step("Добавление булки и создание заказа")
    def create_order(self):
        self.add_ingredient()
        self.click_create_order()

    @allure.step("Закрытие окна заказа")
    def close_modal_window(self):
        self.click_elem(ConstructorLocators.CLOSE_MODAL_BTN)

    @allure.step("Добавляем булку в заказ")
    def add_ingredient(self):
        ingredient = self.find_element(ConstructorLocators.BUNS)
        basket_lst = self.find_element(ConstructorLocators.BASKET)
        self.drag_and_drop_js(ingredient, basket_lst)
        assert self.return_text(ConstructorLocators.BUNS_COUNTER) == '2', f'Фактический результат {self.return_text(ConstructorLocators.BUNS_COUNTER)}'

    @allure.step("Модальное окно открылось")
    def assert_modal_window_details_displayed(self):
        self.click_to_bun()
        assert self.return_text(ConstructorLocators.DESCRIPTION_TITLE) == 'Детали ингредиента'

    @allure.step("Модальное окно закрылось")
    def assert_modal_window_closed(self):
        self.close_modal_window()
        assert self.find_element(ConstructorLocators.DESCRIPTION_TITLE, condition=EC.invisibility_of_element)

    @allure.step("Закрываем модальное окно")
    def assert_redirect_nav_tab(self, url, elem):
        match elem:
            case 'Конструктор':
                self.click_constructor()
                self.assert_redirect_page(url, ConstructorLocators.CONSTRUCTOR_TITLE)
            case 'Лента заказов':
                self.assert_redirect_page(url, ConstructorLocators.ORDERS_TAPE_TITLE)
                self.click_tape_orders()