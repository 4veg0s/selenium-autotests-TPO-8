from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BasePage:
    def __init__(self, driver, url):
        self.base_url = "https://arnypraht.com"
        self.driver = driver
        self.url = self.base_url + url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Открыть страницу"""
        self.driver.get(self.url)

    def find_element(self, locator, timeout=10):
        """Найти элемент с явным ожиданием"""
        try:
            return self.wait.until(EC.presence_of_element_located(locator))

        except TimeoutException:
            raise AssertionError(f"Элемент {locator} не найден за {timeout} секунд")

    def find_nested_element(self, parent_locator, child_locator):
        """Найти вложенный элемент внутри родительского элемента"""
        parent_element = self.find_element(parent_locator)
        return parent_element.find_element(child_locator)

    def get_action_chain(self):
        action = ActionChains(driver=self.driver)
        return action

    def move_to_element(self, locator):
        element = self.find_element(locator)
        return self.get_action_chain().move_to_element(element).perform()

    def click(self, locator):
        """Клик по элементу"""
        element = self.find_element(locator)
        element.click()
        # element.click()

    def input_text(self, locator, text):
        """Ввод текста в элемент"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def press_enter(self, locator):
        """Нажатие энтера"""
        element = self.find_element(locator)
        element.send_keys(Keys.RETURN)

    def is_element_present(self, locator):
        """Проверка присутствия элемента"""
        try:
            self.find_element(locator)
            return True
        except AssertionError:
            return False

    def get_element_text(self, locator):
        """Получить текст элемента"""
        return self.find_element(locator).text

    def is_element_visible(self, locator):
        """Проверка, что элемент видим на странице"""
        element = self.find_element(locator)
        return element.is_displayed()
