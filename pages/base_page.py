from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу")
    def open_window(self, url):
        self.driver.get(url)

    def find_element(self, locator, condition=EC.element_to_be_clickable, time=10):
        return WebDriverWait(self.driver, time).until(condition(locator))

    def waiting_change_value(self, locator, text, time=10, ):
        return WebDriverWait(self.driver, time).until_not(EC.text_to_be_present_in_element(locator, text))

    def find_elements(self, locator, condition=EC.visibility_of_any_elements_located, time=10):
        return WebDriverWait(self.driver, time).until(condition(locator))

    def return_text(self, locator):
        return self.find_element(locator, condition=EC.visibility_of_element_located).text

    # Ввод данных в поле
    def write_in_field(self, input=None, text=None, time=10):
        WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(input)).send_keys(text)

    @allure.step("Проверка URL")
    def assert_url(self, expected_url, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.url_to_be(expected_url))
        except TimeoutException:
            raise AssertionError(f"Проверка URL провалена. Текущий URL: {self.driver.current_url}\n")

    @allure.step("Проверка редиректа на страницу")
    def assert_redirect_page(self, url, locator):
        self.assert_url(url)
        assert self.find_element(locator, condition=EC.visibility_of_element_located).is_displayed() == True

    @allure.step("Клик на элемент по скрипту")
    def click_elem(self, locator):
        element = self.find_element(locator)
        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

    def drag_and_drop_js(self, source_element, target_element):
        """
        Универсальный метод, который имитирует drag&drop средствами JS.
        Вызывается из любого PageObject, не зная о driver напрямую.
        """
        script = """
            const source = arguments[0];
            const target = arguments[1];

            const dataTransfer = new DataTransfer();
            const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragStartEvent);

            const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dragOverEvent);

            const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });
            target.dispatchEvent(dropEvent);

            const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
            source.dispatchEvent(dragEndEvent);
        """
        self.driver.execute_script(script, source_element, target_element)
