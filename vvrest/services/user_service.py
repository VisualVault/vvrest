import requests
from ..constants import USERS_URL, WEB_TOKEN_URL, SITE_ID_URL


class UserService:
    def __init__(self, vault):
        self.vault = vault

    def get_users(self, query=''):
        """
        get all users or search by query
        :param query: string, default: empty string, example: "userId='test@test.com'"
        :return: dict
        """
        request_url = self.vault.base_url + USERS_URL
        if query:
            request_url += '?q=' + query

        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()
        return resp

    def get_user(self, user_id):
        """
        get a single user
        :param user_id: string uuid4
        :return: dict
        """
        endpoint = USERS_URL + '/' + user_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_user_web_token(self, user_id):
        """
        get a users webToken by userId
        :param user_id: string uuid4
        :return: dict
        """
        endpoint = USERS_URL + '/' + user_id + '/' + WEB_TOKEN_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def create_user(self, site_id, user_id, first_name, last_name, email, password):
        """
        create a new user  # TODO: write unit test, report possible bug and report 500 errors give away internal errors
        :param site_id: string uuid4
        :param user_id: string uuid4
        :param first_name: string
        :param last_name: string
        :param email: string
        :param password: string
        :return: dict
        """
        endpoint = USERS_URL + SITE_ID_URL + site_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()

        payload = {
            'userId': user_id,
            'firstName': first_name,
            'lastName': last_name,
            'emailAddress': email,
            'password': password
        }

        resp = requests.post(request_url, headers=headers, data=payload).json()

        return resp

    def update_user(self, user_id, fields_dict):
        """
        update a user
        :param user_id: string uuid4
        :param fields_dict: dict, example: {'enabled': True, 'lastName': 'new name'}
        :return: dict
        """
        endpoint = USERS_URL + '/' + user_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.put(request_url, headers=headers, data=fields_dict).json()

        return resp
