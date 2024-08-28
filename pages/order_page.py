import allure

from locators import OrderPageLocator

from .base_page import BasePage


class OrderPage(BasePage):
    url = BasePage.url + 'order'
    page_locators = OrderPageLocator

    @allure.step('Открыть страницу создания заказа')
    def open_page(self):
        self.driver.get(self.url)

    @allure.step('Заполнить имя в форме')
    def set_name(self, name):
        element = self.find_element(self.page_locators.form_name_input)
        element.click()
        element.send_keys(name)

    @allure.step('Заполнить фамилию в форме')
    def set_last_name(self, last_name):
        element = self.find_element(self.page_locators.form_last_name_input)
        element.click()
        element.send_keys(last_name)

    @allure.step('Заполнить адрес в форме')
    def set_address(self, address):
        element = self.find_element(self.page_locators.form_address_input)
        element.click()
        element.send_keys(address)

    @allure.step('Выбрать станцию метро в форме')
    def set_metro_station(self, metro_station=None):
        element = self.find_element(self.page_locators.form_metro_station_input)
        element.click()
        elements = self.driver.find_elements(*self.page_locators.popup_metro_stations)
        if metro_station:
            for i in range(len(elements)):
                if elements[i].text == metro_station:
                    elements[i].click()
                    return
        elements[0].click()

    @allure.step('Заполнить номер телефона в форме')
    def set_phone_number(self, phone_number):
        element = self.find_element(self.page_locators.form_phone_number_input)
        element.click()
        element.send_keys(phone_number)

    @allure.step('Нажать на кнопку "Далее" в форме')
    def click_button_next(self):
        self.find_element(self.page_locators.form_button_next).click()

    def set_user_info_form(self, **user_data):
        self.set_name(user_data['name'])
        self.set_last_name(user_data['last_name'])
        self.set_address(user_data['address'])
        self.set_metro_station(user_data['metro_station'])
        self.set_phone_number(user_data['phone_number'])

    @allure.step('Выбрать дату доставки в форме')
    def set_delivery_date(self):
        self.find_element(self.page_locators.form_delivery_date_input).click()
        date_picker = self.driver.find_elements(*self.page_locators.date_picker_popup)
        date_picker[0].click()

    @allure.step('Выбрать период в форме')
    def set_period(self):
        self.find_element(self.page_locators.form_rental_period_input).click()
        self.driver.find_elements(*self.page_locators.period_popup)[0].click()

    @allure.step('Выбрать цвет самоката')
    def set_color(self):
        self.find_element(self.page_locators.form_black_color_input).click()

    @allure.step('Заполнить комментарий в форме')
    def set_comment(self, comment):
        element = self.find_element(self.page_locators.form_comment_input)
        element.click()
        element.send_keys(comment)

    @allure.step('Нажать на кнопку "Да" в модальном окне')
    def click_modal_button_create(self):
        self.find_element(self.page_locators.modal_button_create).click()

    @allure.step('Нажать на кнопку "Заказать" в форме')
    def click_button_create(self):
        self.find_element(self.page_locators.form_button_create).click()


    def set_rent_form(self, comment):
        self.set_delivery_date()
        self.set_period()
        self.set_color()
        self.set_comment(comment)

    def check_modal_order_create_success(self):
        return self.find_element(self.page_locators.modal_order_create_success).is_displayed()
