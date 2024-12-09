from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):
    # Локаторы элементов страницы регистрации
    _LOGIN_EMAIL = (By.XPATH, "//input[@id=\"field-5\"]")
    _LOGIN_PASSWORD = (By.XPATH, "//input[@id=\"field-6\"]")

    _REGISTRATION_LINK = (By.LINK_TEXT, "Регистрация")
    _AUTH_BUTTON = (By.XPATH, "//main//button[contains(@class, 'bar__button')]")

    _LOGIN_SUCCESS_MARKER = (By.XPATH, "//h1[text()='Мой аккаунт']")
    _EMPTY_FIELD_ERROR_MESSAGE = (By.XPATH, "//div[contains(@class, \"field__message\") and text()=\"Заполните поле\"]")

    def __init__(self, driver):
        super().__init__(driver, "/login")

    def login(self, email, password):
        """Выполнить авторизацию"""
        self.input_text(self._LOGIN_EMAIL, email)

        self.input_text(self._LOGIN_PASSWORD, password)

        self.click(self._AUTH_BUTTON)

    def is_login_failed(self):
        """Проверка наличия сообщения об ошибке"""
        return self.is_element_present(self._ERROR_MESSAGE)

    def go_to_registration(self):
        """Перейти на страницу регистрации"""
        self.click(self._REGISTRATION_LINK)

    def is_border_bottom_color(self, locator):
        error_color = "rgba(230, 46, 77, 1)"
        try:
            return self.find_element(locator).value_of_css_property("border-bottom-color") == error_color
        except NoSuchElementException:
            return False

    def is_any_border_bottom_red(self):
        """Нижняя граница поля красная"""
        return self.is_border_bottom_color(self._LOGIN_EMAIL) or self.is_border_bottom_color(self._LOGIN_PASSWORD)

    def is_login_successful(self):
        """Проверка перехода в аккаунт"""
        return self.is_element_present(self._LOGIN_SUCCESS_MARKER)
