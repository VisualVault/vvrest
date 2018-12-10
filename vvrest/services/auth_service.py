from ..constants import TOKEN_URL, GRANT_TYPE_PASSWORD, GRANT_TYPE_REFRESH
import requests


class AuthService:
    def __init__(self, url, customer_alias, database_alias, client_id, client_secret):
        """
        :param url:
        :param customer_alias:
        :param database_alias:
        :param client_id:
        :param client_secret:
        """
        self.url = url
        self.customer_alias = customer_alias
        self.database_alias = database_alias
        self.client_id = client_id
        self.client_secret = client_secret

    def get_access_token(self):
        """
        requests access_token
        :return: dict
        """
        request_url = self.url + TOKEN_URL
        headers = {'Content-Type': 'application/json'}

        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'username': self.client_id,
            'password': self.client_secret,
            'grant_type': GRANT_TYPE_PASSWORD
        }

        resp = requests.post(request_url, data=payload, headers=headers).json()

        return resp

    def refresh_access_token(self, refresh_token):
        """
        requests refresh of access_token
        :param refresh_token: string
        :return: dict
        """
        request_url = self.url + TOKEN_URL
        headers = {'Content-Type': 'application/json'}

        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': refresh_token,
            'grant_type': GRANT_TYPE_REFRESH
        }

        resp = requests.post(request_url, data=payload, headers=headers).json()

        return resp
