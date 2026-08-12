import allure
from api.user_api import UserAPI
from helpers import generate_user_data

class TestLoginUser:
    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user_success(self):
        user_data = generate_user_data()
        reg_response = UserAPI.create_user(user_data)
        token = reg_response.json().get("accessToken")

        login_payload = {
            "email": user_data["email"],
            "password": user_data["password"]
        }
        response = UserAPI.login_user(login_payload)

        assert response.status_code == 200
        assert response.json().get("success") is True

        if token:
            UserAPI.delete_user(token)

    @allure.title("Логин с неверным логином и паролем")
    def test_login_wrong_credentials_error(self):
        user_data = generate_user_data()
        login_payload = {
            "email": "wrong_" + user_data["email"],
            "password": "wrong_" + user_data["password"]
        }
        response = UserAPI.login_user(login_payload)

        assert response.status_code == 401
        assert response.json().get("message") == "email or password are incorrect"