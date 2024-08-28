from selenium.webdriver.common.by import By

from .header_locator import HeaderLocator


class MainPageLocator(HeaderLocator):
    __question_locator = '//div[text()="{0}"]//parent::div[@class="accordion__button"]'
    __answer_locator = '//p[text()="{0}"]'

    first_question_text = 'Сколько это стоит? И как оплатить?'
    first_question_locator = By.XPATH, __question_locator.format(first_question_text)
    first_answer_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    first_answer_locator = By.XPATH, __answer_locator.format(first_answer_text)

    second_question_text = 'Хочу сразу несколько самокатов! Так можно?'
    second_question_locator = By.XPATH, __question_locator.format(second_question_text)
    second_answer_text = ('Пока что у нас так: один заказ — один самокат. '
                          'Если хотите покататься с друзьями, '
                          'можете просто сделать несколько заказов — один за другим.')
    second_answer_locator = By.XPATH, __answer_locator.format(second_answer_text)

    third_question_text = 'Как рассчитывается время аренды?'
    third_question_locator = By.XPATH, __question_locator.format(third_question_text)
    third_answer_text = ('Допустим, вы оформляете заказ на 8 мая. '
                         'Мы привозим самокат 8 мая в течение дня. '
                         'Отсчёт времени аренды начинается с момента, '
                         'когда вы оплатите заказ курьеру. '
                         'Если мы привезли самокат 8 мая в 20:30,'
                         ' суточная аренда закончится 9 мая в 20:30.')
    third_answer_locator = By.XPATH, __answer_locator.format(third_answer_text)

    four_question_text = 'Можно ли заказать самокат прямо на сегодня?'
    four_question_locator = By.XPATH, __question_locator.format(four_question_text)
    four_answer_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    four_answer_locator = By.XPATH, __answer_locator.format(four_answer_text)

    five_question_text = 'Можно ли продлить заказ или вернуть самокат раньше?'
    five_question_locator = By.XPATH, __question_locator.format(five_question_text)
    five_answer_text = ('Пока что нет! Но если что-то срочное '
                        '— всегда можно позвонить в поддержку по красивому номеру 1010.')
    five_answer_locator = By.XPATH, __answer_locator.format(five_answer_text)

    six_question_text = 'Вы привозите зарядку вместе с самокатом?'
    six_question_locator = By.XPATH, __question_locator.format(six_question_text)
    six_answer_text = ('Самокат приезжает к вам с полной зарядкой. '
                       'Этого хватает на восемь суток — '
                       'даже если будете кататься без передышек и во сне. '
                       'Зарядка не понадобится.')
    six_answer_locator = By.XPATH, __answer_locator.format(six_answer_text)

    seven_question_text = 'Можно ли отменить заказ?'
    seven_question_locator = By.XPATH, __question_locator.format(seven_question_text)
    seven_answer_text = ('Да, пока самокат не привезли. '
                         'Штрафа не будет, объяснительной записки тоже не попросим. '
                         'Все же свои.')
    seven_answer_locator = By.XPATH, __answer_locator.format(seven_answer_text)

    eighth_question_text = 'Я жизу за МКАДом, привезёте?'
    eighth_question_locator = By.XPATH, __question_locator.format(eighth_question_text)
    eighth_answer_text = ('Да, обязательно. Всем самокатов! '
                          'И Москве, и Московской области.')
    eighth_answer_locator = By.XPATH, __answer_locator.format(eighth_answer_text)

    questions_answers = {
        first_question_locator: first_answer_locator,
        second_question_locator: second_answer_locator,
        third_question_locator: third_answer_locator,
        four_question_locator: four_answer_locator,
        five_question_locator: five_answer_locator,
        six_question_locator: six_answer_locator,
        seven_question_locator: seven_answer_locator,
        eighth_question_locator: eighth_answer_locator
    }

    button_order_create = By.CSS_SELECTOR, '[class ="Button_Button__ra12g Button_Middle__1CSJM"]'
