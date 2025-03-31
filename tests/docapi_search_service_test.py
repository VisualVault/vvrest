import unittest

from vvrest.services.docapi_search_service import DocApiSearchService

from .utilities import get_vault_object, get_parameters_json


class DocApiSearchServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
            cls.vault = get_vault_object()

        test_parameters = get_parameters_json()
        cls.document_id = test_parameters['document_id']
        cls.document_revision_id = test_parameters['document_revision_id']
        cls.folder_id = test_parameters['folder_id']
        cls.bad_folder_id = 'notauuid'
        cls.invalid_folder_id = '123f98aa-4cc4-4dd4-9cab-12350ccc5e73'
        cls.vault_jwt = get_vault_object(user_web_token=None, jwt=None, auto_jwt=True)
        cls.vault_jwt_not_enabled = get_vault_object(user_web_token=None, jwt=None, auto_jwt=True, docapi_enabled=False)

    def test_docapi_not_enabled(self):
        """
        validates docapi calls will not be made w/o a jwt
        """
        with self.assertRaises(Exception) as ex:
            DocApiSearchService(self.vault_jwt_not_enabled)

        self.assertEqual(str(ex.exception), 'docapi is not enabled for this vv environment')
    
    def test_doc_api_get_document_invalid(self):
        """
        validates 400 is returned if not a valid folder id
        """
        doc_service = DocApiSearchService(self.vault_jwt)
        resp = doc_service.get_documents_by_folder(self.invalid_folder_id)
        self.assertLessEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']['documents']), 0)

        doc_service = DocApiSearchService(self.vault_jwt)
        bad_resp = doc_service.get_documents_by_folder(self.bad_folder_id)
        self.assertLessEqual(bad_resp['meta']['status'], 400)

    def test_doc_api_get_documents_by_folder(self):
        """
        validates successful retrieval of documents by folder
        """
        doc_service = DocApiSearchService(self.vault_jwt)

        resp_all_docs = doc_service.get_documents_by_folder(self.folder_id)
        self.assertIsNotNone(resp_all_docs['data'])
        self.assertEqual(resp_all_docs['meta']['status'], 200)
        self.assertGreaterEqual(len(resp_all_docs['data']['documents']), 5)

        resp = doc_service.get_documents_by_folder(self.folder_id, take=5, page=0)
        self.assertIsNotNone(resp['data'])
        self.assertEqual(resp['meta']['status'], 200)
        self.assertLessEqual(len(resp['data']['documents']), 5)

        resp_p2 = doc_service.get_documents_by_folder(self.folder_id, take=5, page=1)
        self.assertIsNotNone(resp_p2['data'])
        self.assertEqual(resp_p2['meta']['status'], 200)
        self.assertLessEqual(len(resp_p2['data']['documents']), 5)
        
        self.assertNotEqual(resp['data']['documents'][0]['dhRev'], resp_p2['data']['documents'][0]['dhRev'])


    def test_doc_api_get_documents_by_folder_with_sort(self):
        """
        validates retrieval of documents with sorting parameters
        """
        doc_service = DocApiSearchService(self.vault_jwt)

        # asc
        resp = doc_service.get_documents_by_folder(self.folder_id, sort_by='dhRev', sort_direction='asc')
        self.assertIsNotNone(resp['data'])
        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']['documents']), 0)

        # desc
        desc_resp = doc_service.get_documents_by_folder(self.folder_id, sort_by='dhRev', sort_direction='desc')
        self.assertIsNotNone(desc_resp['data'])
        self.assertEqual(desc_resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']['documents']), 0)
        
        self.assertNotEqual(resp['data']['documents'][0]['dhRev'], desc_resp['data']['documents'][0]['dhRev'])
    
    def test_doc_api_get_documents_by_folder_with_archive_type(self):
        """
        validates retrieval of documents with archiveType parameter
        """
        doc_service = DocApiSearchService(self.vault_jwt)
        resp = doc_service.get_documents_by_folder(self.folder_id, archive_type=0)
        self.assertIsNotNone(resp['data'])
        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']['documents']), 0)

        resp_archived = doc_service.get_documents_by_folder(self.folder_id, archive_type=1)
        self.assertIsNotNone(resp_archived['data'])
        self.assertEqual(resp_archived['meta']['status'], 200)
        self.assertEqual(len(resp_archived['data']['documents']), 0)

    def test_doc_api_get_documents_by_folder_with_role_security(self):
        """
        validates retrieval of documents with roleSecurity parameter
        """
        doc_service = DocApiSearchService(self.vault_jwt)
        resp = doc_service.get_documents_by_folder(self.folder_id, role_security=True)
        self.assertIsNotNone(resp['data'])
        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']['documents']), 0)
    
    def test_doc_api_get_documents_by_folder_without_role_security(self):
        """
        validates retrieval of documents without roleSecurity parameter
        """
        doc_service = DocApiSearchService(self.vault_jwt)
        resp = doc_service.get_documents_by_folder(self.folder_id)
        self.assertIsNotNone(resp['data'])
        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']['documents']), 0)
    
    def test_doc_api_get_documents_by_folder_with_search_query(self):
        """
        validates retrieval of documents using search query
        """
        doc_service = DocApiSearchService(self.vault_jwt)
        resp = doc_service.get_documents_by_folder(self.folder_id, q="[dlId] eq '" + self.document_id + "'")
        self.assertIsNotNone(resp['data'])
        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']['documents']), 0)
        self.assertEqual(resp['data']['documents'][0]['dlId'], self.document_id)
