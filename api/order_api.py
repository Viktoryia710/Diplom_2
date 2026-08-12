import requests
from urls import URL

class OrderAPI:
    @staticmethod
    def create_order(payload, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        return requests.post(URL.CREATE_ORDER, json=payload, headers=headers)

    @staticmethod
    def get_user_orders(token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        return requests.get(URL.GET_ORDERS, headers=headers)

    @staticmethod
    def get_ingredients():
        return requests.get(URL.GET_INGREDIENTS)