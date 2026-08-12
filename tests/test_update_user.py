import pytest
import allure
from api.user_api import UserAPI
from helpers import generate_user_data, generate_random_string

class TestUpdateUser:
    @allure.title("Изменение данных пользователя с авторизацией")
    @pytest.mark.parametrize("field_to_update", ["email", "name"])
    def test_update_user_with_auth_success(self, field_to_update):
        user_data = generate_user_data()
        reg_resp = UserAPI.create_user(user_data)
        token = reg_resp.json().get("accessToken")

        new_value = f"new_{generate_random_string()}@yandex.ru" if field_to_update == "email" else f"NewName_{generate_random_string()}"
        update_payload = {field_to_update: new_value}

        response = UserAPI.update_user(update_payload, token=token)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert response.json()["user"][field_to_update] == new_value

        if token:
            UserAPI.delete_user(token)

    @allure.title("Изменение данных пользователя без авторизации")
    def test_update_user_without_auth_error(self):
        update_payload = {"name": "NewNameWithoutAuth"}
        response = UserAPI.update_user(update_payload, token=None)

        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"