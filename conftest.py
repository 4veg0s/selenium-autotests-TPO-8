import os
import pytest
import yaml
from selenium import webdriver


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
    driver = webdriver.Chrome()

    # Настройка размера окна
    driver.maximize_window()

    yield driver

    # Закрытие браузера после теста
    driver.quit()
