class Token:
    def __init__(self, access_token, token_expiration, refresh_token):
        """
        :param access_token: string
        :param token_expiration: datetime
        :param refresh_token: string
        """
        self.access_token = access_token
        self.token_expiration = token_expiration
        self.refresh_token = refresh_token
