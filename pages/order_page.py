from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[contains(@class,'select-search__select')]//div[text()='{}']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DROPDOWN = (By.XPATH, "//span[@class='Dropdown-arrow']")
    RENT_OPTION = (By.XPATH, "//div[@class='Dropdown-menu']//div[text()='{}']")
    BLACK_CHECKBOX = (By.ID, "black")
    GREY_CHECKBOX = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class,'Order_Buttons')]//button[not(contains(@class,'Inverted')) and text()='Заказать']")
    ORDER_HEADER = (By.XPATH, "//div[contains(@class,'Order_Header')]")
    
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_HEADER = (By.XPATH, "//div[contains(@class,'Order_ModalHeader')]")

    def fill_step1(self, name, surname, address, metro, phone):
        self.send_keys(self.NAME_INPUT, name)
        self.send_keys(self.SURNAME_INPUT, surname)
        self.send_keys(self.ADDRESS_INPUT, address)
        self.click(self.METRO_INPUT)
        metro_locator = (By.XPATH, self.METRO_OPTION[1].format(metro))
        self.click(metro_locator)
        self.send_keys(self.PHONE_INPUT, phone)
        self.click(self.NEXT_BUTTON)

    def fill_step2(self, date, rent_period, color, comment):
        self.send_keys(self.DATE_INPUT, date)
        self.click(self.ORDER_HEADER)
        self.click(self.RENT_DROPDOWN)
        rent_locator = (By.XPATH, self.RENT_OPTION[1].format(rent_period))
        self.click(rent_locator)
        if color == "black":
            self.click(self.BLACK_CHECKBOX)
        elif color == "grey":
            self.click(self.GREY_CHECKBOX)
        if comment:
            self.send_keys(self.COMMENT_INPUT, comment)
        self.click(self.ORDER_BUTTON)

    def confirm_order(self):
        self.click(self.CONFIRM_BUTTON)

    def is_order_success(self):
        return "Заказ оформлен" in self.wait_visible(self.SUCCESS_HEADER).text
