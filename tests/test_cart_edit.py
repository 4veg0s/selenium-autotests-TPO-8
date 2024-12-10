import time

import pytest

from pages.cart_edit_page import CartEditPage


class TestEditCart:
    def test_edit_filled_cart_success(self, browser):
        edit_cart_page = CartEditPage(browser)

        edit_cart_page.open_shop()
        edit_cart_page.init_catalog_cards()

        edit_cart_page.fill_cart()

        edit_cart_page.open_cart()
        time.sleep(5)
        edit_cart_page.init_cart_cards()

        assert edit_cart_page.is_item_added_successfully(), "Есть несовпадения по товарам в корзине"

        # assert edit_cart_page.is_item_added_successfully(item), f"Товар '{item['name']} ({item['color']})' не найден"

        # edit_cart_page.clear_cart()
