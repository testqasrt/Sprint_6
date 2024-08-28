import allure
import pytest

from locators import MainPageLocator
from pages import MainPage


class TestQuestionAnswer:
    question_answer = (
        (MainPageLocator.first_question_locator, MainPageLocator.first_answer_text),
        (MainPageLocator.second_question_locator, MainPageLocator.second_answer_text),
        (MainPageLocator.third_question_locator, MainPageLocator.third_answer_text),
        (MainPageLocator.four_question_locator, MainPageLocator.four_answer_text),
        (MainPageLocator.five_question_locator, MainPageLocator.five_answer_text),
        (MainPageLocator.six_question_locator, MainPageLocator.six_answer_text),
        (MainPageLocator.seven_question_locator, MainPageLocator.seven_answer_text),
        (MainPageLocator.eighth_question_locator, MainPageLocator.eighth_answer_text)
    )

    @pytest.mark.parametrize('question, answer_text', question_answer)
    @allure.title('Проверка текста ответа на вопрос')
    def test_answer_correct_text(self, driver, question, answer_text):
        main_page = MainPage(driver)
        main_page.open_page()
        main_page.scroll_and_click_on_question(question)
        answer_element = main_page.get_answer_element(question)
        assert main_page.check_display_answer(answer_element)
        assert main_page.get_answer_text(answer_element) == answer_text

