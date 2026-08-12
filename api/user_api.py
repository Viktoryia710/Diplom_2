import requests
from urls import URL

class UserAPI:
    @staticmethod
    def create_user(payload):
        return requests.post(URL.CREATE_USER, json=payload)

    @staticmethod
    def login_user(payload):
        return requests.post(URL.LOGIN_USER, json=payload)

    @staticmethod
    def update_user(payload, token=None):
        headers = {}
        if token:
            headers["Authorization"] = token
        return requests.patch(URL.USER_DATA, json=payload, headers=headers)

    @staticmethod
    def delete_user(token):
        headers = {"Authorization": token}
        return requests.delete(URL.USER_DATA, headers=headers)