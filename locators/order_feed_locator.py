from selenium.webdriver.common.by import By


class OrdersFeedLocators:

    FIRST_ORDER_ID = (By.XPATH, '(//ul[contains(@class,"OrderFeed_list__OLh59")]//a[contains(@class,"OrderHistory_link__1iNby")])[1]')
    COMPOUND_TITLE = (By.XPATH, '//p[@class="text text_type_main-medium mb-8"]')
    ORDER_ID = (By.XPATH, '//p[@class="text text_type_digits-default"]')
    COUNT_ALL_TIMES = [By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"OrderFeed_number__2MbrQ")]']
    COUNT_TODAY = [By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number__2MbrQ")]']
    ORDER_IN_WORKS = [By.XPATH, '//ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li']