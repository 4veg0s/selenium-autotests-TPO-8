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

        assert not registration_page.is_registration_failed(), "Сообщение об ошибке не отображается"

    @pytest.mark.parametrize("invalid_email", [
        # "invalid_email",
        # "email@",
        "@domain.com",
        # "a" * 100 + "@domain.com"
    ])
    def test_registration_invalid_email(self, browser, invalid_email):
        registration_page = RegistrationPage(browser)
        registration_page.open()

        registration_page.register_user(
            email=invalid_email,
            phone="79898989898",
            password="StrongPass123!"
        )

        assert registration_page.is_any_border_bottom_red(), "Сообщение об ошибке отображается"
