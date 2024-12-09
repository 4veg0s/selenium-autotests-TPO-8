import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FilterShopPage(BasePage):
    _CARD_LOCATOR = (By.XPATH, "//div[@class='card card--ready']")
    _CARD_SUBTITLE_COLOR_LOCATOR = (By.XPATH, "//div[contains(@class, 'card__subtitle')]")
    _FILTER_BUTTON = (By.XPATH, "//button[@data-filter-bar-opener]")
    _FILTER_COLOR_CHECKBOX_BLACK = (By.XPATH, "//span[contains(@class, 'donut__bg') and contains(@class, 'black')]/following-sibling::span[contains(@class, 'checkbox__tick')]")
    _FILTER_CLOSE_BUTTON = (By.XPATH, "//button[@class='cross']")

    def __init__(self, driver):
        super().__init__(driver, "/shop")

    def filter_black_items(self):
        """Выполнить поиск"""
        self.move_to_element(self._FILTER_BUTTON)
        self.click(self._FILTER_BUTTON)
        self.move_to_element(self._FILTER_COLOR_CHECKBOX_BLACK)
        self.click(self._FILTER_COLOR_CHECKBOX_BLACK)
        self.move_to_element(self._FILTER_CLOSE_BUTTON)
        self.click(self._FILTER_CLOSE_BUTTON)
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 500)")

    def are_all_items_found_truly_black(self):
        target_color = 'черный'
        cards = self.find_elements(self._CARD_LOCATOR)
        return all([target_color in str.lower(self.get_nested_element_text(card, self._CARD_SUBTITLE_COLOR_LOCATOR)) for card in cards])
