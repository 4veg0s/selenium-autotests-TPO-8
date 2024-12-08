import os
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Загрузка конфигурации из YAML файла
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


@pytest.fixture(scope='session')
def config():
    return load_config()


@pytest.fixture(scope='function')
def browser(config):
    """Фикстура для настройки и запуска браузера"""
    browser_name = config['browser']['default']
    headless_mode = config['browser']['headless']

    driver = webdriver.Chrome()

    # Настройка размера окна
    driver.maximize_window()

    yield driver

    # Закрытие браузера после теста
    driver.quit()