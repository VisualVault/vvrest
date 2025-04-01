import unittest

from .utilities import get_vault_object
from vvrest.services.config_service import ConfigService


class ConfigServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
            cls.vault = get_vault_object()

    def test_docapi_config_enabled(self):
        """
        tests ConfigService.get_docapi_config enabled
        """
        config_service = ConfigService(self.vault)
        resp = config_service.get_docapi_config()

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['isEnabled'], True)
