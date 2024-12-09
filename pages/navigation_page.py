from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NavigationPage(BasePage):
    # Локаторы элементов страницы регистрации
    _BAGS_LINK = (By.XPATH, "//ul[@class='header__menu']//a[@href='/category/bags/']")
    _BACKPACKS_LINK = (By.XPATH, "//ul[@class='header__menu']//a[@href='/category/backpacks/']")
    _ACCESSORIES_LINK = (By.XPATH, "//ul[@class='header__menu']//a[@href='/category/aksessuary/']")
    _CLOTHING_LINK = (By.XPATH, "//ul[@class='header__menu']//a[@href='/shop/clothes/']")

    _BAGS_SUCCESS_MARKER = (By.XPATH, "//h1[@class='spoiler__title' and text()='Сумки']")
    _BACKPACKS_SUCCESS_MARKER = (By.XPATH, "//h1[@class='spoiler__title' and text()='Рюкзаки']")
    _ACCESSORIES_SUCCESS_MARKER = (By.XPATH, "//h1[@class='spoiler__title' and text()='Аксессуары']")
    _CLOTHING_SUCCESS_MARKER = (By.XPATH, "//h1[@class='spoiler__title' and text()='Одежда']")

    def __init__(self, driver):
        super().__init__(driver, "/")

    def navigate_to_bags(self):
        """Перейти в соответсвующий раздел"""
        self.move_to_element(self._BAGS_LINK)
        self.click(self._BAGS_LINK)

    def navigate_to_backpacks(self):
        """Перейти в соответсвующий раздел"""
        self.move_to_element(self._BACKPACKS_LINK)
        self.click(self._BACKPACKS_LINK)

    def navigate_to_accessories(self):
        """Перейти в соответсвующий раздел"""
        self.move_to_element(self._ACCESSORIES_LINK)
        self.click(self._ACCESSORIES_LINK)

    def navigate_to_clothing(self):
        """Перейти в соответсвующий раздел"""
        self.move_to_element(self._CLOTHING_LINK)
        self.click(self._CLOTHING_LINK)

    def is_bags_opened_successfully(self):
        """Проверка перехода в соответсвующий раздел"""
        return self.is_element_present(self._BAGS_SUCCESS_MARKER)

    def is_backpacks_opened_successfully(self):
        """Проверка перехода в соответсвующий раздел"""
        return self.is_element_present(self._BACKPACKS_SUCCESS_MARKER)

    def is_accessories_opened_successfully(self):
        """Проверка перехода в соответсвующий раздел"""
        return self.is_element_present(self._ACCESSORIES_SUCCESS_MARKER)

    def is_clothing_opened_successfully(self):
        """Проверка перехода в соответсвующий раздел"""
        return self.is_element_present(self._CLOTHING_SUCCESS_MARKER)
