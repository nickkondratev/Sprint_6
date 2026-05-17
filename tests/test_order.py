import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:
    
    @allure.title('Позитивный сценарий заказа самоката')
    @allure.description('Полный флоу заказа с двумя наборами данных')
    @pytest.mark.parametrize('entry_point, name, surname, address, metro, phone, date, rent, color, comment', [
        ('top', 'Иван', 'Иванов', 'Москва, Ленина 1', 'Сокольники', '79991112233', '01.06.2026', 'сутки', 'black', 'Комментарий 1'),
        ('bottom', 'Петр', 'Петров', 'Москва, Гагарина 5', 'Лубянка', '79994445566', '15.06.2026', 'двое суток', 'grey', 'Комментарий 2'),
    ])
    def test_order_scooter(self, driver, entry_point, name, surname, address, metro, phone, date, rent, color, comment):
        main = MainPage(driver)
        order = OrderPage(driver)
        
        main.open()
        main.accept_cookies()
        
        if entry_point == 'top':
            main.click_order_top()
        else:
            main.click_order_bottom()
        
        order.fill_step1(name, surname, address, metro, phone)
        order.fill_step2(date, rent, color, comment)
        order.confirm_order()
        assert order.is_order_success(), "Заказ не оформлен"

    @allure.title('Переход по логотипу Самоката')
    def test_scooter_logo(self, driver):
        main = MainPage(driver)
        main.open()
        main.accept_cookies()
        main.click_order_top()
        main.click_scooter_logo()
        assert driver.current_url == MainPage.URL, "Не перешли на главную"

    @allure.title('Переход по логотипу Яндекса')
    def test_yandex_logo(self, driver):
        main = MainPage(driver)
        main.open()
        main.accept_cookies()
        main.click_yandex_logo()
        
        handles = driver.window_handles
        assert len(handles) > 1, "Новая вкладка не открылась"
        driver.switch_to.window(handles[1])
        WebDriverWait(driver, 10).until(lambda d: d.current_url != 'about:blank')
        assert "dzen.ru" in driver.current_url or "ya.ru" in driver.current_url, f"URL: {driver.current_url}"
