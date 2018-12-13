import unittest
from .utilities import get_vault_object
from vvrest.services.form_service import FormService


class FormServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()

    def test_get_forms(self):
        """
        tests FormService.get_form_templates
        """
        form_service = FormService(self.vault)
        resp = form_service.get_form_templates()

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 0)
