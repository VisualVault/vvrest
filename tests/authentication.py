import unittest
from .utilities import get_vault_object


class AuthenticationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()

    def test_access_token(self):
        """
        validates authentication
        """
        self.assertIsNotNone(self.vault.token.access_token)
        self.assertGreater(len(self.vault.token.access_token), 0)

    def test_refresh_token(self):
        """
        validates refresh_token functionality
        """
        access_token = str(self.vault.token.access_token)
        self.assertGreater(len(access_token), 0)
        self.vault.refresh_token()
        self.assertGreater(len(self.vault.token.access_token), 0)
        self.assertNotEqual(access_token, self.vault.token.access_token)
