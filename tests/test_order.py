import allure
import pytest
from data.data import ORDER_DATA_TOP, ORDER_DATA_BOTTOM
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Позитивный сценарий заказа через верхнюю кнопку')
    def test_order_scooter_top(self, driver):
        main = MainPage(driver)
        order = OrderPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main.open()
            main.accept_cookies()
        
        with allure.step('Нажать верхнюю кнопку Заказать'):
            main.click_order_top()
        
        with allure.step('Заполнить форму заказа'):
            order.fill_step1(
                ORDER_DATA_TOP['name'],
                ORDER_DATA_TOP['surname'],
                ORDER_DATA_TOP['address'],
                ORDER_DATA_TOP['metro'],
                ORDER_DATA_TOP['phone']
            )
            order.fill_step2(
                ORDER_DATA_TOP['date'],
                ORDER_DATA_TOP['rent'],
                ORDER_DATA_TOP['color'],
                ORDER_DATA_TOP['comment']
            )
            order.confirm_order()
        with allure.step('Проверить успешное оформление'):
            assert order.is_order_success(), "Заказ не оформлен"

    @allure.title('Позитивный сценарий заказа через нижнюю кнопку')
    def test_order_scooter_bottom(self, driver):
        main = MainPage(driver)
        order = OrderPage(driver)
        
        with allure.step('Открыть главную страницу'):
            main.open()
            main.accept_cookies()
        
        with allure.step('Нажать нижнюю кнопку Заказать'):
            main.click_order_bottom()
        
        with allure.step('Заполнить форму заказа'):
            order.fill_step1(
                ORDER_DATA_BOTTOM['name'],
                ORDER_DATA_BOTTOM['surname'],
                ORDER_DATA_BOTTOM['address'],
                ORDER_DATA_BOTTOM['metro'],
                ORDER_DATA_BOTTOM['phone']
            )
            order.fill_step2(
                ORDER_DATA_BOTTOM['date'],
                ORDER_DATA_BOTTOM['rent'],
                ORDER_DATA_BOTTOM['color'],
                ORDER_DATA_BOTTOM['comment']
            )
            order.confirm_order()
        
        with allure.step('Проверить успешное оформление'):
            assert order.is_order_success(), "Заказ не оформлен"

    @allure.title('Переход по логотипу Самоката')
    def test_scooter_logo(self, driver):
        main = MainPage(driver)
        
        with allure.step('Открыть страницу и перейти к заказу'):
            main.open()
            main.accept_cookies()
            main.click_order_top()
            main.click_scooter_logo()
        
        with allure.step('Проверить URL'):
            assert main.get_current_url() == MainPage.URL, "Не перешли на главную"

    @allure.title('Переход по логотипу Яндекса')
    def test_yandex_logo(self, driver):
        main = MainPage(driver)
        
        with allure.step('Открыть страницу и нажать логотип Яндекса'):
            main.open()
            main.accept_cookies()
            main.click_yandex_logo()
        
        with allure.step('Переключиться на новую вкладку'):
            main.switch_to_window(1)
        
        with allure.step('Проверить URL'):
            url = main.wait_url_loaded()
            assert "yandex.ru" in url, f"URL: {url}"
