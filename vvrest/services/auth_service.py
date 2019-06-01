from ..constants import TOKEN_URL, GRANT_TYPE_PASSWORD, GRANT_TYPE_REFRESH
import requests


class AuthService:
    def __init__(self, url, customer_alias, database_alias, client_id, client_secret, user_web_token):
        """
        :param url: string, example: https://demo.visualvault.com
        :param customer_alias: string
        :param database_alias: string
        :param client_id: string UUID(version=4)
        :param client_secret: string, example: khN18YAZPe6F3Z0tc2W0HXCb487jm0wgwe6kNffUNf0=
        :param user_web_token: string UUID(version=4), passed in if authentication is user impersonation
        """
        self.url = url
        self.customer_alias = customer_alias
        self.database_alias = database_alias
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_web_token = user_web_token

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
            'grant_type': GRANT_TYPE_PASSWORD
        }

        if self.user_web_token:  # impersonation
            payload['username'] = self.user_web_token
            payload['password'] = self.user_web_token
        else:
            payload['username'] = self.client_id
            payload['password'] = self.client_secret

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
