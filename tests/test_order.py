import allure
import pytest

from pages import MainPage, OrderPage


class TestOrder:
    user_data = (
        {
            'name': 'Имя',
            'last_name': 'Фамилия',
            'address': 'Город Улица',
            'metro_station': '',
            'phone_number': '89685591100'
        },
        {
            'name': 'ИмяОдин',
            'last_name': 'ФамилияОдин',
            'address': 'Город УлицаОдин',
            'metro_station': 'Преображенская площадь',
            'phone_number': '89685591101'
        },
    )

    @staticmethod
    def open_main_page(driver):
        main_page = MainPage(driver)
        main_page.open_page()
        return main_page

    @pytest.mark.parametrize('main_page_method',
                             ('click_header_order_button', 'click_order_button'))
    @pytest.mark.parametrize('user_data', (user_data[0], user_data[1]))
    @allure.title('Создание заказа при переходе с главной страницы')
    def test_order_create(self, driver, main_page_method, user_data):
        main_page = self.open_main_page(driver)
        getattr(main_page, main_page_method)()
        assert driver.current_url == OrderPage.url

        order_page = OrderPage(driver)
        order_page.set_user_info_form(**user_data)
        order_page.click_button_next()
        order_page.set_rent_form('Комментарий')
        order_page.click_button_create()
        order_page.click_modal_button_create()
        assert order_page.check_modal_order_create_success()

