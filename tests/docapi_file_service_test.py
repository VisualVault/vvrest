import unittest

from vvrest.services.docapi_file_service import DocApiFileService

from .utilities import get_vault_object, get_parameters_json


class DocApiFileServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
            cls.vault = get_vault_object()

        test_parameters = get_parameters_json()
        cls.document_id = test_parameters['document_id']
        cls.document_revision_id = test_parameters['document_revision_id']
        cls.vault_jwt = get_vault_object(user_web_token=None, jwt=None)
        cls.vault_jwt_not_enabled = get_vault_object(user_web_token=None, jwt=None, docapi_enabled=False)

    def test_docapi_file_not_enabled(self):
        """
        validates docapi file calls will not be made w/o a jwt
        """
        with self.assertRaises(Exception) as ex:
            DocApiFileService(self.vault_jwt_not_enabled)

        self.assertEqual(str(ex.exception), 'docapi is not enabled for this vv environment')

    def test_docapi_get_file_404(self):
        """
        validates 404 is returned if not a valid dhid
        """
        file_service = DocApiFileService(self.vault_jwt)
        resp = file_service.get_file_stream(self.document_id)
        self.assertEqual(resp.status_code, 404)

    def test_docapi_get_file_stream(self):
        """
        validates successful doc api file stream call
        """
        file_service = DocApiFileService(self.vault_jwt)
        resp = file_service.get_file_stream(self.document_revision_id)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.text, 'test file')
