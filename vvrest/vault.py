from .token import Token
from .utilities import get_token_expiration
from .services.auth_service import AuthService


class Vault:
    def __init__(self, url, customer_alias, database_alias, client_id, client_secret, user_web_token=None):
        """
        if user_web_token is passed in, then vv will authenticate on behalf of the user that
        the web_token belongs to. if user_web_token is not passed in (default=None), then
        vv will authenticate on behalf of the user that the client_id and client_secret belong to.
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
        self.token = self.get_access_token()
        self.base_url = self.get_base_url()

    def get_access_token(self):
        """
        requests access token
        :return: Token
        """
        authentication_service = AuthService(self.url, self.customer_alias, self.database_alias, self.client_id,
                                             self.client_secret, self.user_web_token)

        resp = authentication_service.get_access_token()
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

    def refresh_access_token(self):
        """
        void method that refreshes Vault.token
        :return: None
        """
        authentication_service = AuthService(self.url, self.customer_alias, self.database_alias, self.client_id,
                                             self.client_secret, self.user_web_token)

        resp = authentication_service.refresh_access_token(self.token.refresh_token)
        access_token = resp['access_token']
        token_expiration = get_token_expiration(resp['expires_in'])
        refresh_token = resp['refresh_token']
        self.token = Token(access_token, token_expiration, refresh_token)

    def get_auth_headers(self):
        """
        :return: dict
        """
        headers = {'Authorization': 'Bearer ' + self.token.access_token}

        return headers
