import pytest

from pages.filter_page import FilterShopPage


class TestShopFilter:
    def test_filter_catalog(self, browser):
        filter_shop_page = FilterShopPage(browser)
        filter_shop_page.open()
        filter_shop_page.filter_black_items()

        assert filter_shop_page.are_all_items_found_truly_black(), "Не все товары черного цвета"
