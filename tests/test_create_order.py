import allure
from api.user_api import UserAPI
from api.order_api import OrderAPI
from helpers import generate_user_data

class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_with_auth_and_ingredients_success(self):
        user_data = generate_user_data()
        reg_resp = UserAPI.create_user(user_data)
        token = reg_resp.json().get("accessToken")

        ingredients_resp = OrderAPI.get_ingredients()
        ingredient_id = ingredients_resp.json()["data"][0]["_id"]

        order_payload = {"ingredients": [ingredient_id]}
        response = OrderAPI.create_order(order_payload, token=token)

        assert response.status_code == 200
        assert response.json().get("success") is True

        if token:
            UserAPI.delete_user(token)

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth_success(self):
        ingredients_resp = OrderAPI.get_ingredients()
        ingredient_id = ingredients_resp.json()["data"][0]["_id"]

        order_payload = {"ingredients": [ingredient_id]}
        response = OrderAPI.create_order(order_payload, token=None)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_without_ingredients_error(self):
        order_payload = {"ingredients": []}
        response = OrderAPI.create_order(order_payload, token=None)

        assert response.status_code == 400
        assert response.json().get("message") == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_invalid_ingredient_hash_error(self):
        order_payload = {"ingredients": ["invalid_hash_12345"]}
        response = OrderAPI.create_order(order_payload, token=None)

        assert response.status_code == 500