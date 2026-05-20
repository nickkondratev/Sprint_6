import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Найти элемент по локатору')
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    @allure.step('Дождаться видимости элемента')
    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step('Кликнуть по элементу')
    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step('Прокрутить до элемента и кликнуть через JS')
    def click_by_js(self, locator):
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получить текст элемента')
    def text(self, locator):
        return self.find(locator).text

    @allure.step('Ввести текст в поле')
    def send_keys(self, locator, value):
        self.find(locator).send_keys(value)

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Переключиться на вкладку {index}')
    def switch_to_window(self, index):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[index])

    @allure.step('Дождаться загрузки страницы')
    def wait_url_loaded(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != 'about:blank')
        return self.driver.current_url
