from selenium.webdriver.common.by import By


class ConstructorLocators:

    CONSTRUCTOR_TITLE = (By.XPATH, '//h1[@class="text text_type_main-large mb-5 mt-10"]')
    CONSTRUCTOR_BTN = (By.XPATH, '//p[contains(text(), "Конструктор")]')
    ORDERS_TAPE_TITLE = (By.XPATH, '//h1[@class="text text_type_main-large mt-10 mb-5"]')
    ORDERS_TAPE_BTN = (By.XPATH, '//p[contains(text(), "Лента Заказов")]')
    ORDER_ID = (By.XPATH, '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    BUNS = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]')
    BUNS_COUNTER = (By.XPATH, '(//div[contains(@class, "counter_counter__ZNLkj")]//p[contains(@class, "counter_counter__num__3nue1")])[2]')
    STUFFING_TAB = (By.XPATH, '//span[contains(text(), "Начинки"]')
    MEAT = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6f"]')
    BASKET = (By.XPATH, '//div[@class="constructor-element constructor-element_pos_top"]')
    DESCRIPTION_TITLE = (By.XPATH, '//h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"]')
    CLOSE_MODAL_BTN = (By.XPATH, '//section[@class="Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]/div/button')
    CREATE_ORDER_BTN = (By.XPATH, '//button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]')
    ORDER_STATUS = (By.XPATH, '//p[@class="undefined text text_type_main-small mb-2"]')