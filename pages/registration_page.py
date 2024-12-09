import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    # Локаторы элементов страницы авторизации
    _REGISTER_EMAIL = (By.ID, "office-auth-register-email")
    _REGISTER_PHONE = (By.ID, "office-auth-register-mobilephone")
    _REGISTER_PASSWORD = (By.ID, "office-register-form-password")

    _REGISTER_BIRTH_DAY = (By.XPATH, "//select[@name=\"birth_day\"]")
    _REGISTER_BIRTH_DAY_LI = (By.XPATH, "//li[contains(@id, \"birth_day\") and text()=\"01\"]")
    _REGISTER_BIRTH_MONTH = (By.XPATH, "//span[contains(@id, \"birth_month\")]") # "//select[@name=\"birth_month\"]")
    _REGISTER_BIRTH_MONTH_LI = (By.XPATH, "//li[contains(@id, \"birth_month\") and text()=\"Янв\"]")
    _REGISTER_BIRTH_YEAR = (By.XPATH, "//span[contains(@id, \"birth_year\")]")
    _REGISTER_BIRTH_YEAR_LI = (By.XPATH, "//li[contains(@id, \"birth_year\") and text()=\"1995\"]")

    _AGREE_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    _AUTH_LINK = (By.LINK_TEXT, "Авторизация")
    _REGISTER_BUTTON = (By.XPATH, "//button[@type='submit' and @data-analytics='register']")
    _EMPTY_FIELD_ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, \"field__message\") and text()=\"Заполните поле\"]")

    def __init__(self, driver):
        super().__init__(driver, "/register")

    def register_user(self, email, phone, password):
        """Выполнить регистрацию"""
        self.driver.execute_script("window.scrollTo(0, 300)")

        self.input_text(self._REGISTER_EMAIL, email)

        self.input_text(self._REGISTER_PHONE, phone)

        self.input_text(self._REGISTER_PASSWORD, password)

        self.click(self._REGISTER_BIRTH_DAY)
        self.click(self._REGISTER_BIRTH_DAY_LI)
        self.click(self._REGISTER_BIRTH_MONTH)
        self.click(self._REGISTER_BIRTH_MONTH_LI)
        self.click(self._REGISTER_BIRTH_YEAR)
        self.click(self._REGISTER_BIRTH_YEAR_LI)
        self.click(self._AGREE_CHECKBOX)

        self.click(self._REGISTER_BUTTON)

    def is_registration_failed(self):
        """Проверка наличия сообщения об ошибке"""
        return self.is_element_present(self._EMPTY_FIELD_ERROR_MESSAGE)

    def is_any_border_bottom_red(self):
        """Нижняя граница поля красная"""
        return self.is_border_bottom_color(self._REGISTER_EMAIL) or self.is_border_bottom_color(
            self._REGISTER_PHONE) or self.is_border_bottom_color(self._REGISTER_PASSWORD)

    def go_to_auth(self):
        """Перейти на страницу авторизации"""
        self.click(self._AUTH_LINK)

    def is_border_bottom_color(self, locator):
        error_color = "#e62e4d"
        try:
            return self.find_element(locator).value_of_css_property("border-bottom-color") == error_color
        except NoSuchElementException:
            return False
