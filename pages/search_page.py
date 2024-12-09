import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


def get_xpath_locator_for_item_name(item_name):
    return (By.XPATH, f"//div[@class='card card--ready']//div[@class='card__panel']//div[contains(@class, 'card__title') and text()='{item_name}']")


def get_xpath_locator_for_item_color(item_color):
    return (By.XPATH, f"//div[@class='card card--ready']//div[@class='card__panel']//div[contains(@class, 'card__subtitle') and text()='{item_color}']")


class SearchPage(BasePage):
    # Локатор кнопки поиска
    _SEARCH_BUTTON = (By.XPATH, "//button[@class='sign search-page-invisible']")
    _SEARCH_FIELD = (By.XPATH, "//div[contains(@class, 'dropdown')]//input[@name='query']")

    def __init__(self, driver):
        super().__init__(driver, "/")

    def search_item(self, item):
        """Выполнить поиск"""
        self.move_to_element(self._SEARCH_BUTTON)
        self.click(self._SEARCH_BUTTON)
        self.move_to_element(self._SEARCH_FIELD)
        self.input_text(self._SEARCH_FIELD, item['name'] + ' ' + item['color'])
        self.press_enter(self._SEARCH_FIELD)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")

    def is_item_found_successfully(self, item):
        """Проверка перехода в соответсвующий раздел"""
        return self.is_element_present(get_xpath_locator_for_item_name(item['name'])) and self.is_element_present(
            get_xpath_locator_for_item_color(item['color']))
