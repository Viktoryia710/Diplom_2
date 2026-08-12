import allure
from api.user_api import UserAPI
from api.order_api import OrderAPI
from helpers import generate_user_data

class TestGetUserOrders:
    @allure.title("Получение заказов конкретного авторизованного пользователя")
    def test_get_orders_authorized_user_success(self):
        user_data = generate_user_data()
        reg_resp = UserAPI.create_user(user_data)
        token = reg_resp.json().get("accessToken")

        ingredients_resp = OrderAPI.get_ingredients()
        ingredient_id = ingredients_resp.json()["data"][0]["_id"]
        OrderAPI.create_order({"ingredients": [ingredient_id]}, token=token)

        response = OrderAPI.get_user_orders(token=token)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "orders" in response.json()

        if token:
            UserAPI.delete_user(token)

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_orders_unauthorized_user_error(self):
        response = OrderAPI.get_user_orders(token=None)

        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"