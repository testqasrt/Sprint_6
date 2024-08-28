from selenium.webdriver.common.by import By

from .header_locator import HeaderLocator


class OrderPageLocator(HeaderLocator):
    _form_input_locator = './/input[@placeholder="{0}"]'

    form_name_input = By.XPATH, _form_input_locator.format('* Имя')
    form_last_name_input = By.XPATH, _form_input_locator.format('* Фамилия')
    form_address_input = By.XPATH, _form_input_locator.format('* Адрес: куда привезти заказ')
    form_metro_station_input = By.XPATH, _form_input_locator.format('* Станция метро')
    form_phone_number_input = By.XPATH, _form_input_locator.format('* Телефон: на него позвонит курьер')

    form_delivery_date_input = By.XPATH, _form_input_locator.format('* Когда привезти самокат')
    form_rental_period_input = By.XPATH, './/div[text()="* Срок аренды"]'
    form_black_color_input = By.CSS_SELECTOR, 'input[id="black"]'
    form_comment_input = By.XPATH, _form_input_locator.format('Комментарий для курьера')

    _form_button_locator = '.// button[text() = "{0}"]'
    form_button_next = By.XPATH, _form_button_locator.format('Далее')
    form_button_create = By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text() = "Заказать"]'

    popup_metro_stations = By.XPATH, '//ul[@class="select-search__options"]//li'

    date_picker_popup = (By.XPATH,
                         '//div[@class="react-datepicker__month-container"]/div[@class="react-datepicker__month"]/div')

    period_popup = By.XPATH, '//div[@class="Dropdown-menu"]'
    modal_locator = '//div[@class="Order_Modal__YZ-d3"]'
    modal_button_create = By.XPATH, f'{modal_locator}/div/button[text()="Да"]'
    modal_order_create_success = By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]'