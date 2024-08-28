from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import \
    expected_conditions as expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    url = 'https://qa-scooter.praktikum-services.ru/'
    timeout = 30

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def driver(self):
        return self._driver

    def _await(self, locator):
        WebDriverWait(self.driver, self.timeout).until(expected_conditions.visibility_of_element_located(locator))

    def find_element(self, locator):
        self._await(locator)
        return self.driver.find_element(*locator)



