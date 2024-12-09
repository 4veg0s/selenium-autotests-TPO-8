from pages.navigation_page import NavigationPage
import time


class TestNavigation:
    def test_navigate_to_bags_success(self, browser):
        navigation_page = NavigationPage(browser)
        navigation_page.open()
        navigation_page.navigate_to_bags()

        assert navigation_page.is_bags_opened_successfully(), "Раздел сумок не открылся"

    def test_navigate_to_backpacks_success(self, browser):
        navigation_page = NavigationPage(browser)
        navigation_page.open()
        navigation_page.navigate_to_backpacks()

        assert navigation_page.is_backpacks_opened_successfully(), "Раздел рюкзаков не открылся"

    def test_navigate_to_accessories_success(self, browser):
        navigation_page = NavigationPage(browser)
        navigation_page.open()
        navigation_page.navigate_to_accessories()

        assert navigation_page.is_accessories_opened_successfully(), "Раздел аксессуаров не открылся"

    def test_navigate_to_clothing_success(self, browser):
        navigation_page = NavigationPage(browser)
        navigation_page.open()
        navigation_page.navigate_to_clothing()

        time.sleep(3)

        assert navigation_page.is_clothing_opened_successfully(), "Раздел одежды не открылся"
