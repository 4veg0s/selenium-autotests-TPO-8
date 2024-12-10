import time

import pytest

from pages.cart_edit_page import CartEditPage


class TestEditCart:
    def test_edit_cart_item_quantity_success(self, browser):
        edit_cart_page = CartEditPage(browser)

        edit_cart_page.open_shop()
        edit_cart_page.init_catalog_cards()

        edit_cart_page.fill_cart()

        edit_cart_page.open_cart()
        time.sleep(5)
        edit_cart_page.init_cart_cards()
        assert edit_cart_page.is_item_added_successfully(), "Есть несовпадения по товарам в корзине"

        edit_cart_page.add_quantity_to_cart_element()
        assert edit_cart_page.has_item_quantity_increased_successfully(), "Количество товара не стало равным 2"

    def test_edit_cart_delete_item_success(self, browser):
        edit_cart_page = CartEditPage(browser)

        edit_cart_page.open_shop()
        time.sleep(5)
        edit_cart_page.init_catalog_cards()

        edit_cart_page.fill_cart()

        edit_cart_page.open_cart()
        time.sleep(5)
        edit_cart_page.init_cart_cards()
        assert edit_cart_page.is_item_added_successfully(), "Есть несовпадения по товарам в корзине"

        edit_cart_page.delete_item_from_cart()
        assert edit_cart_page.is_element_absent_from_cart(), "Товар не удалился из корзины"


        # assert edit_cart_page.is_item_added_successfully(item), f"Товар '{item['name']} ({item['color']})' не найден"

        # edit_cart_page.clear_cart()
