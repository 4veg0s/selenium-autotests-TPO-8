import random
import string

import pytest
from utils.data_generator import generate_user_data
from pages.registration_page import RegistrationPage


class TestRegistration:
    def test_successful_registration(self, browser):
        # Подготовка тестовых данных
        user_data = generate_user_data()

        # Шаги теста
        registration_page = RegistrationPage(browser)
        registration_page.open()
        registration_page.register_user(
            email=user_data['email'],
            phone=user_data['phone'],
            password=user_data['password']
        )

        assert registration_page.is_registration_success_visible(), "Не отображается благодарность за регистрацию"

    @pytest.mark.parametrize("invalid_email", [
        "invalid_email",
        "email@",
        "@domain.com",
        str(random.choice(string.ascii_lowercase) * 100) + "@domain.com"   # Превышает 100 символов (регистрация проходит)
    ])
    def test_registration_invalid_email(self, browser, invalid_email):
        registration_page = RegistrationPage(browser)
        registration_page.open()
        user_data = generate_user_data()

        registration_page.register_user(
            email=invalid_email,
            phone=user_data['phone'],
            password=user_data['password']
        )

        assert not registration_page.is_registration_success_visible(), "Благодарность за регистрацию отображается"
        assert registration_page.is_any_border_bottom_red(), "Поле не подсвечено красным"
