import unittest
from .utilities import get_vault_object
from pytz import timezone


class AuthServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
            cls.vault = get_vault_object()

    def test_access_token(self):
        """
        tests AuthService.get_access_token
        """
        self.assertIsNotNone(self.vault.token.access_token)
        self.assertGreater(len(self.vault.token.access_token), 0)
        self.assertGreater(len(self.vault.token.refresh_token), 0)
        self.assertEqual(self.vault.token.token_expiration.tzinfo, timezone('UTC'))

    def test_refresh_access_token(self):
        """
        tests AuthService.refresh_access_token
        """
        access_token = str(self.vault.token.access_token)
        self.assertGreater(len(access_token), 0)
        self.vault.refresh_access_token()
        self.assertGreater(len(self.vault.token.access_token), 0)
        self.assertNotEqual(access_token, self.vault.token.access_token)
        self.assertGreater(len(self.vault.token.refresh_token), 0)
        self.assertEqual(self.vault.token.token_expiration.tzinfo, timezone('UTC'))
