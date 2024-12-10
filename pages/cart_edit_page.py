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

    _CLEAR_CART_BUTTON = (By.XPATH, "//button[@value='cart/clean']")

    def __init__(self, driver):
        self.catalog_cards_slice = None
        self.add_to_cart_buttons_slice = None
        self.cart_cards = None
        super().__init__(driver, "/")

    def init_catalog_cards(self):
        cards = self.find_elements(self._CARD_LOCATOR)
        add_to_cart_buttons = self.find_elements(self._ADD_TO_CART_BUTTON)
        self.catalog_cards_slice = cards[:3]  # срез для 3-х первых товаров из каталога
        self.add_to_cart_buttons_slice = add_to_cart_buttons[:3]  # срез для 3-х первых товаров из каталога

    def init_cart_cards(self):
        self.cart_cards = self.find_elements(self._CART_TABLE_ELEMENT)

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

    def edit_cart(self):
        pass

    def open_shop(self):
        self.driver.get(self.base_url + self._SHOP_URL)
        time.sleep(3)

    def open_cart(self):
        self.driver.get(self.base_url + self._CART_URL)

    def is_item_added_successfully(self):   # FIXME: не работает
        """Проверка, что все элеменгты были добавлены в корзину"""
        return all(
            [(str.lower(self.find_nested_element(self.catalog_cards_slice[i], self._CART_TABLE_PRODUCT_NAME).text) ==
              str.lower(self.find_nested_element(self.cart_cards[i], self._CARD_TITLE_NAME_LOCATOR).text)
              and
              str.lower(self.find_nested_element(self.catalog_cards_slice[i], self._CART_TABLE_PRODUCT_COLOR).text) ==
              str.lower(self.find_nested_element(self.cart_cards[i], self._CARD_SUBTITLE_COLOR_LOCATOR).text)
              ) for i in range(len(self.catalog_cards_slice))])

    def are_all_items_found_truly_black(self):
        target_color = 'черный'
        cards = self.find_elements(self._CARD_LOCATOR)
        return all(
            [target_color in str.lower(self.get_nested_element_text(card, self._CARD_SUBTITLE_COLOR_LOCATOR)) for card
             in cards])
