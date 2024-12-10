import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


def get_xpath_locator_for_item_name(item_name):
    return (By.XPATH,
            f"//div[@class='card card--ready']//div[@class='card__panel']//div[contains(@class, 'card__title') and text()='{item_name}']")


def get_xpath_locator_for_item_color(item_color):
    return (By.XPATH,
            f"//div[@class='card card--ready']//div[@class='card__panel']//div[contains(@class, 'card__subtitle') and text()='{item_color}']")


class AddToCardPage(BasePage):
    # Локатор кнопки поиска
    _SEARCH_BUTTON = (By.XPATH, "//button[@class='sign search-page-invisible']")
    _SEARCH_FIELD = (By.XPATH, "//div[contains(@class, 'dropdown')]//input[@name='query']")
    _ADD_TO_CART_BUTTON = (By.XPATH, "//button[@value='cart/add']")
    _GO_TO_CART_BUTTON = (By.XPATH, "//div[@class='note__body']//a[@href='/cart/']")

    _CART_TABLE_PRODUCT_NAME = (
    By.XPATH, "//div[contains(@class, 'cart-table__r')]//div[@class='cart-table__descr']//div[@class='h6']")
    _CART_TABLE_PRODUCT_COLOR = (By.XPATH,
                                 "//div[contains(@class, 'cart-table__r')]//div[@class='cart-table__descr']//div[contains(@class,'color-name')]")

    _CLEAR_CART_BUTTON = (By.XPATH, "//button[@value='cart/clean']")

    def __init__(self, driver):
        super().__init__(driver, "/")

    def search_and_add_item_to_cart(self, item):
        """Выполнить поиск"""
        self.move_to_element(self._SEARCH_BUTTON)
        self.click(self._SEARCH_BUTTON)
        self.move_to_element(self._SEARCH_FIELD)
        self.input_text(self._SEARCH_FIELD, item['name'] + ' ' + item['color'])
        self.press_enter(self._SEARCH_FIELD)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")

        self.move_to_element(self._ADD_TO_CART_BUTTON)
        self.click(self._ADD_TO_CART_BUTTON)
        time.sleep(2)

        self.move_to_element(self._GO_TO_CART_BUTTON)
        self.click(self._GO_TO_CART_BUTTON)

    def is_item_added_successfully(self, item):
        """Проверка перехода в соответсвующий раздел"""
        return (self.find_element(self._CART_TABLE_PRODUCT_NAME).text == item['name'] and
                self.find_element(self._CART_TABLE_PRODUCT_COLOR).text == item['color'])

    def clear_cart(self):
        """Очистить корзину"""
        self.move_to_element(self._CLEAR_CART_BUTTON)
        self.click(self._CLEAR_CART_BUTTON)
