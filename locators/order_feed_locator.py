from selenium.webdriver.common.by import By


class OrdersFeedLocators:

    FIRST_ORDER_ID = (By.XPATH, '(//ul[contains(@class,"OrderFeed_list__OLh59")]//a[contains(@class,"OrderHistory_link__1iNby")])[1]')
    COMPOUND_TITLE = (By.XPATH, '//p[@class="text text_type_main-medium mb-8"]')
    ORDER_ID = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    COUNT_ALL_TIMES = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"OrderFeed_number__2MbrQ")]']
    COUNT_TODAY = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number__2MbrQ")]']
    ORDER_IN_WORKS = [By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li']
    ORDER_ID = (By.XPATH,
                '//h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    ORDERS_ID_IN_HISTORY = (By.XPATH,
                            '(//li[contains(@class,"OrderHistory_listItem__2x95r")])[1]//div[contains(@class,"OrderHistory_textBox__3lgbs")]//p[1]')