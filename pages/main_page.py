import allure
from selenium.webdriver.remote.webelement import WebElement

from locators import MainPageLocator
from pages.base_page import BasePage


class MainPage(BasePage):
    page_locators = MainPageLocator

    @allure.step('Открыть главную страницу')
    def open_page(self):
        self.driver.get(self.url)

    @allure.step('Кликнуть на вопрос')
    def scroll_and_click_on_question(self, question):
        element = self.find_element(question)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self._await(question)
        element.click()

    def get_answer_element(self, question: WebElement) -> WebElement:
        return self.find_element(self.page_locators.questions_answers[question])

    @allure.step('Кликнуть на кнопку создания заказа в хэдере')
    def click_header_order_button(self):
        element = self.find_element(self.page_locators.header_button_order_create)
        self._await(self.page_locators.header_button_order_create)
        element.click()

    @allure.step('Кликнуть на кнопку создания заказа на главной странице')
    def click_order_button(self):
        element = self.find_element(self.page_locators.button_order_create)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self._await(self.page_locators.button_order_create)
        element.click()

    @staticmethod
    def check_display_answer(answer_element: WebElement) -> bool:
        return answer_element.is_displayed()

    @staticmethod
    def get_answer_text(answer_element: WebElement) -> str:
        return answer_element.text

