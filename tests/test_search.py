import pytest

from pages.search_page import SearchPage


class TestSearch:
    @pytest.mark.parametrize("item", [
        {"name": "MOVE S", "color": "черный + Оливье"},
        {"name": "VENDI 11", "color": "серо-зеленый металлик"},
        {"name": "POUCH", "color": "черный"},
        {"name": "Топ TUSA", "color": "Розово-красный"}
    ])
    def test_search_item_success(self, browser, item):
        search_page = SearchPage(browser)
        search_page.open()
        search_page.search_item(item)

        assert search_page.is_item_found_successfully(item), f"Товар '{item['name']} ({item['color']})' не найден"
