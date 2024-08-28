import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def driver():
    _driver = webdriver.Firefox()
    _driver.maximize_window()
    yield _driver
    _driver.quit()

