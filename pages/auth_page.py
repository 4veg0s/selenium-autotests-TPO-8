from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AuthPage(BasePage):
    # Локаторы элементов страницы авторизации
    _LOGIN_EMAIL = (By.ID, "login-email")
    _LOGIN_PASSWORD = (By.ID, "login-password")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    _REGISTRATION_LINK = (By.LINK_TEXT, "Регистрация")
    _ERROR_MESSAGE = (By.CLASS_NAME, "error-message")

    def __init__(self, driver):
        super().__init__(driver, "/login")

    def login(self, email, password):
        """Выполнить авторизацию"""
        self.input_text(self._LOGIN_EMAIL, email)
        self.input_text(self._LOGIN_PASSWORD, password)
        self.click(self._LOGIN_BUTTON)

    def is_login_failed(self):
        """Проверка наличия сообщения об ошибке"""
        return self.is_element_present(self._ERROR_MESSAGE)

    def go_to_registration(self):
        """Перейти на страницу регистрации"""
        self.click(self._REGISTRATION_LINK)
