import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartEditPage(BasePage):
    _SHOP_URL = "/shop"
    _CART_URL = "/cart"

    _CARD_LOCATOR = (By.XPATH, "//div[contains(@class, 'card--ready')]")
    _CARD_TITLE_NAME_LOCATOR = (By.XPATH, "//div[contains(@class, 'card__title')]")
    _CARD_SUBTITLE_COLOR_LOCATOR = (By.XPATH, "//div[contains(@class, 'card__subtitle')]")

    _ADD_TO_CART_BUTTON = (By.XPATH, "//button[@value='cart/add']")
    _CLOSE_NOTE_BUTTON = (By.XPATH, "//button[@class='note__cross cross']")

    _GO_TO_CART_BUTTON = (By.XPATH, "//div[@class='note__body']//a[@href='/cart/']")
    _CART_TABLE_ELEMENT = (By.XPATH, "//div[@data-cart-item]")
    _CART_TABLE_PRODUCT_NAME = (By.XPATH, "//div[@class='h6']")
    _CART_TABLE_PRODUCT_COLOR = (By.XPATH, "//div[contains(@class,'color-name')]")

    _QUANTITY_INPUT_COUNTER = (By.XPATH, "//input[@data-quantity-input]")
    _QUANTITY_ADD_BUTTON = (By.XPATH, "//button[@data-quantity-plus]")

    _DELETE_CART_ELEMENT_BUTTON = (By.XPATH, "//button[@data-cart-remove]")

    _CLEAR_CART_BUTTON = (By.XPATH, "//button[@value='cart/clean']")

    def __init__(self, driver):
        self.cart_card_names = None
        self.cart_card_colors = None
        self.card_names = None
        self.card_colors = None
        self.catalog_cards_slice = None
        self.add_to_cart_buttons_slice = None
        self.cart_cards = None
        super().__init__(driver, "/")

    def init_catalog_cards(self):
        cards = self.find_elements(self._CARD_LOCATOR)
        self.card_names = [element.text for element in self.find_elements(self._CARD_TITLE_NAME_LOCATOR)]
        self.card_colors = [element.text for element in self.find_elements(self._CARD_SUBTITLE_COLOR_LOCATOR)]
        add_to_cart_buttons = self.find_elements(self._ADD_TO_CART_BUTTON)
        self.catalog_cards_slice = cards[:3]  # срез для 3-х первых товаров из каталога
        self.add_to_cart_buttons_slice = add_to_cart_buttons[:3]  # срез для 3-х первых товаров из каталога
        # P.S. первый элемент каталога в какой-то момент распродался и там больше нет кнопки добавить в корзину,
        # поэтому расхождение по срезам

    def init_cart_cards(self):
        self.cart_cards = self.find_elements(self._CART_TABLE_ELEMENT)
        self.cart_card_names = [element.text for element in self.find_elements(self._CART_TABLE_PRODUCT_NAME)]
        self.cart_card_colors = [element.text for element in self.find_elements(self._CART_TABLE_PRODUCT_COLOR)]
        assert len(self.cart_cards) == len(self.catalog_cards_slice)

    def fill_cart(self):
        self.driver.execute_script("window.scrollTo(0, 500)")

        for i in range(len(self.catalog_cards_slice)):
            self.move_to_explicit_element(self.catalog_cards_slice[i])
            self.move_to_explicit_element(self.add_to_cart_buttons_slice[i])
            self.click_explicit(self.add_to_cart_buttons_slice[i])
            time.sleep(1)
            self.move_to_element(self._CLOSE_NOTE_BUTTON)
            self.click(self._CLOSE_NOTE_BUTTON)
            time.sleep(1)

    def add_quantity_to_cart_element(self):
        self.move_to_element(self._QUANTITY_ADD_BUTTON)
        self.click(self._QUANTITY_ADD_BUTTON)
        time.sleep(1)

    def has_item_quantity_increased_successfully(self):
        return self.find_element(self._QUANTITY_INPUT_COUNTER).get_attribute("value") == "2"

    def delete_item_from_cart(self):
        delete_element_buttons = self.find_elements(self._DELETE_CART_ELEMENT_BUTTON)
        self.move_to_explicit_element(delete_element_buttons[1])
        self.click_explicit(delete_element_buttons[1])
        time.sleep(1)

    def is_element_absent_from_cart(self):
            try:
                self.find_element((By.XPATH, f"//div[@class='h6' and text()='{self.cart_card_names[1]}']"))
                self.find_element((By.XPATH, f"//div[contains(@class,'color-name') and text()='{self.cart_card_colors[1]}']"))
                return False
            except AssertionError:
                return True

    def open_shop(self):
        self.driver.get(self.base_url + self._SHOP_URL)
        time.sleep(3)

    def open_cart(self):
        self.driver.get(self.base_url + self._CART_URL)

    def is_item_added_successfully(self):
        """Проверка, что все элементы были добавлены в корзину"""
        # P.S. первый элемент каталога в какой-то момент распродался и там больше нет кнопки добавить в корзину,
        # поэтому расхождение по срезам
        return all(
            [(str.lower(self.card_names[i]) ==
              str.lower(self.cart_card_names[i]))
              and
             (str.lower(self.card_colors[i]) ==
              str.lower(self.cart_card_colors[i]))
             for i in range(len(self.catalog_cards_slice))])
