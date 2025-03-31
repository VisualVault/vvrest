import unittest

from vvrest.services.docapi_document_service import DocApiDocumentService

from .utilities import get_vault_object, get_parameters_json


class DocApiDocumentServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
            cls.vault = get_vault_object()

        test_parameters = get_parameters_json()
        cls.document_id = test_parameters['document_id']
        cls.document_revision_id = test_parameters['document_revision_id']
        cls.vault_jwt = get_vault_object(user_web_token=None, jwt=None, auto_jwt=True)
        cls.vault_jwt_not_enabled = get_vault_object(user_web_token=None, jwt=None, auto_jwt=True, docapi_enabled=False)

    def test_docapi_not_enabled(self):
        """
        validates docapi calls will not be made w/o a jwt
        """
        with self.assertRaises(Exception) as ex:
            DocApiDocumentService(self.vault_jwt_not_enabled)

        self.assertEqual(str(ex.exception), 'docapi is not enabled for this vv environment')
    
    def test_docapi_get_document_404(self):
        """
        validates 404 is returned if not a valid dhid
        """
        doc_service = DocApiDocumentService(self.vault_jwt)
        resp = doc_service.get_document_revision(self.document_id)
        self.assertIsNone(resp['data'])
        self.assertEqual(resp['meta']['status'], 404)

    def test_docapi_get_document_revision(self):
        """
        validates successful doc api doc rev call
        """
        doc_service = DocApiDocumentService(self.vault_jwt)
        resp = doc_service.get_document_revision(self.document_revision_id)
        self.assertIsNotNone(resp['data'])
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['dhId'], self.document_revision_id)
