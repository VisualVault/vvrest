import unittest
from .utilities import get_vault_object, get_test_email_address, get_parameters_json
from vvrest.services.email_service import EmailService


class EmailServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
            cls.vault = get_vault_object()

        test_parameters = get_parameters_json()
        cls.document_revision_id = test_parameters['document_revision_id']
        cls.email_address = get_test_email_address()

    def test_send_email_with_out_attachments(self):
        """
        tests EmailService.send_email without attachments
        """
        email_service = EmailService(self.vault)
        resp = email_service.send_email(self.email_address, self.email_address, 'unittest subject',
                                        'unittest description', False, [])

        self.assertEqual(resp['meta']['status'], 201)

    def test_send_email_with_attachments(self):
        """
        tests EmailService.send_email with attachments
        """
        email_service = EmailService(self.vault)
        resp = email_service.send_email(self.email_address, self.email_address, 'unittest subject',
                                        'unittest description', True, [self.document_revision_id])

        self.assertEqual(resp['meta']['status'], 201)
