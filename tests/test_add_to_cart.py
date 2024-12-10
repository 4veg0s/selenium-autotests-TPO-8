import pytest

from pages.add_to_cart_page import AddToCardPage


class TestAddToCart:
    @pytest.mark.parametrize("item", [
        {"name": "MOVE S", "color": "черный + Оливье"},
        {"name": "VENDI 11", "color": "серо-зеленый металлик"},
        {"name": "POUCH", "color": "черный"},
        {"name": "Топ TUSA", "color": "Розово-красный"}
    ])
    def test_add_item_to_cart_success(self, browser, item):
        add_to_cart_page = AddToCardPage(browser)
        add_to_cart_page.open()
        add_to_cart_page.search_and_add_item_to_cart(item)

        assert add_to_cart_page.is_item_added_successfully(item), f"Товар '{item['name']} ({item['color']})' не найден"

        add_to_cart_page.clear_cart()
