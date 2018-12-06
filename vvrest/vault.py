import requests
from .token import Token
from .utilities import get_token_expiration
from .constants import TOKEN_URL, GRANT_TYPE_PASSWORD, GRANT_TYPE_REFRESH


class Vault:
    def __init__(self, url, customer_alias, database_alias, client_id, client_secret):
        """
        :param url: string, example: https://demo.visualvault.com
        :param customer_alias: string
        :param database_alias: string
        :param client_id: string UUID(version=4)
        :param client_secret: string, example: khN18YAZPe6F3Z0tc2W0HXCb487jm0wgwe6kNffUNf0=
        """
        self.url = url
        self.customer_alias = customer_alias
        self.database_alias = database_alias
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = self.get_token()
        self.base_url = self.get_base_url()

    def get_token(self):
        """
        handles vv authentication
        :return: Token
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
        access_token = resp['access_token']
        token_expiration = get_token_expiration(resp['expires_in'])
        refresh_token = resp['refresh_token']
        token = Token(access_token, token_expiration, refresh_token)

        return token

    def get_base_url(self):
        """
        :return: string
        """
        base_url = self.url + '/api/v1/' + self.customer_alias + '/' + self.database_alias + '/'

        return base_url

    def refresh_token(self):
        """
        void method that refreshes Vault.token
        :return: None
        """
        request_url = self.url + TOKEN_URL
        headers = {'Content-Type': 'application/json'}

        payload = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.token.refresh_token,
            'grant_type': GRANT_TYPE_REFRESH
        }

        resp = requests.post(request_url, data=payload, headers=headers).json()
        access_token = resp['access_token']
        token_expiration = get_token_expiration(resp['expires_in'])
        refresh_token = resp['refresh_token']
        self.token = Token(access_token, token_expiration, refresh_token)
