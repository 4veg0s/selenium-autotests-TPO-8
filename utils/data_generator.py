import random
import string
import faker


def generate_user_data():
    """Генерация данных для регистрации"""
    fake = faker.Faker('ru_RU')

    return {
        'email': fake.email(),
        'password': generate_strong_password(),
        'name': fake.name(),
        'phone': fake.phone_number()
    }


def generate_strong_password(length=12):
    """Генерация надежного пароля"""
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = '!@#$%^&*_+-=[]{}|'

    password = (
            random.choice(uppercase) +
            random.choice(lowercase) +
            random.choice(digits) +
            random.choice(special_chars) +
            ''.join(random.choice(string.ascii_letters + digits + special_chars)
                    for _ in range(length - 4))
    )

    return ''.join(random.sample(password, len(password)))
