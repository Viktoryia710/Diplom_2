import random
import string

def generate_random_string(length=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_user_data():
    email = f"user_{generate_random_string()}@yandex.ru"
    password = f"pass_{generate_random_string()}"
    name = f"Name_{generate_random_string()}"
    return {
        "email": email,
        "password": password,
        "name": name
    }