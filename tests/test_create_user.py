import pytest
import allure
from api.user_api import UserAPI
from helpers import generate_user_data

class TestCreateUser:
    @allure.title("Успешное создание уникального пользователя")
    def test_create_unique_user_success(self):
        user_data = generate_user_data()
        response = UserAPI.create_user(user_data)
        
        assert response.status_code == 200
        assert response.json().get("success") is True
        
        token = response.json().get("accessToken")
        if token:
            UserAPI.delete_user(token)

    @allure.title("Ошибка при создании пользователя, который уже зарегистрирован")
    def test_create_existing_user_error(self):
        user_data = generate_user_data()
        first_resp = UserAPI.create_user(user_data)
        token = first_resp.json().get("accessToken")

        response = UserAPI.create_user(user_data)
        
        assert response.status_code == 403
        assert response.json().get("message") == "User already exists"

        if token:
            UserAPI.delete_user(token)

    @allure.title("Ошибка при создании пользователя без одного из обязательных полей")
    @pytest.mark.parametrize("missing_field", ["email", "password", "name"])
    def test_create_user_missing_field_error(self, missing_field):
        user_data = generate_user_data()
        del user_data[missing_field]

        response = UserAPI.create_user(user_data)
        
        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"