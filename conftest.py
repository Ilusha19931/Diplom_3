import pytest
import helper
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage
from pages.order_feed_page import OrdersFeedPage
from pages.recovery_pass_page import RecoverPasswordPage
from pages.private_account_page import PryvateAccountPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = helper.WebDriverFactory.create_driver(browser)
    driver.maximize_window()
    yield driver
    driver.quit()

def pytest_collection_modifyitems(session, config, items):
    order = [
        'test_orders_feed_page.py',
        'test_constructor_page.py',
        'test_personal_account_page.py',
        'test_recover_password_page.py'
    ]
    def get_file_order(item):
        for idx, name in enumerate(order):
            if name in item.nodeid:
                return idx
        return len(order)

    items.sort(key=get_file_order)


@pytest.fixture()
def recover_password_page(driver):
    page = RecoverPasswordPage(driver)
    return page

@pytest.fixture()
def personal_acc_page(driver):
    page = PryvateAccountPage(driver)
    return page


@pytest.fixture()
def constructor_page(driver):
    page = ConstructorPage(driver)
    return page

@pytest.fixture()
def tape_orders_page(driver):
    page = OrdersFeedPage(driver)
    return page

@pytest.fixture()
def login_page(driver):
    page = LoginPage(driver)
    return page

@pytest.fixture
def open_url():
    def _open(page, url):
        page.open_window(url)
        return page
    return _open