import time

import pytest

from pages.auth_page import AuthPage
from utils.data_generator import generate_user_data
from conftest import config


class TestRegistration:
    def test_successful_login(self, browser, config):
        # Подготовка тестовых данных
        user_data = {
            'email': config['test_data']['valid_user']['email'],
            'password': config['test_data']['valid_user']['password']
        }

        # Шаги теста
        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.login(
            email=user_data['email'],
            password=user_data['password']
        )

        time.sleep(3)

        assert auth_page.is_login_successful(), "Переход в мой аккаунт не произошел"
        # assert not auth_page.is_any_border_bottom_red(), "Включена подсветка полей"

    @pytest.mark.parametrize("invalid_email", [
        "email@domain.com",
    ])
    def test_login_invalid_email(self, browser, invalid_email):
        user_data = generate_user_data()

        auth_page = AuthPage(browser)
        auth_page.open()
        auth_page.login(
            email=invalid_email,
            password=user_data['password']
        )

        assert not auth_page.is_login_successful(), "Переход в мой аккаунт произошел"
        # assert auth_page.is_any_border_bottom_red(), "Не включена подсветка полей"
