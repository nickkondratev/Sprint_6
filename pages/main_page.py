from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    URL = "https://qa-scooter.praktikum-services.ru/"
    
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class,'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class,'Home_FinishButton')]//button")
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class,'LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class,'LogoYandex')]")
    
    FAQ_QUESTION = (By.XPATH, "//div[@id='accordion__heading-{}']")
    FAQ_ANSWER = (By.XPATH, "//div[@id='accordion__panel-{}']//p")

    def open(self):
        self.driver.get(self.URL)

    def accept_cookies(self):
        try:
            self.click(self.COOKIE_BUTTON)
        except Exception:
            pass

    def click_order_top(self):
        self.click(self.ORDER_BUTTON_TOP)

    def click_order_bottom(self):
        locator = self.ORDER_BUTTON_BOTTOM
        element = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)


    def click_faq(self, index):
        locator = (By.XPATH, self.FAQ_QUESTION[1].format(index))
        element = self.find(locator)

        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def get_faq_answer(self, index):
        locator = (By.XPATH, self.FAQ_ANSWER[1].format(index))
        return self.wait_visible(locator).text

    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)

    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
