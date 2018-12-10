import unittest
from .utilities import get_vault_object
from vvrest.services.email_service import EmailService


class EmailTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()
        cls.email_address = 'jared.runyon@visualvault.com'
        cls.document_revision_id = '8fefa9b6-56fa-e811-a995-a3d452a1c2f6'

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
