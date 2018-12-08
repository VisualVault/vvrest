import unittest
from .utilities import get_vault_object, generate_random_uuid
from vvrest.endpoints.documents import Document


class DocumentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()
        cls.folder_path = '/test'
        cls.query_string = "folderPath='/test'"
        cls.document_id = '810013e6-50fa-e811-a9cf-8b72d90dd505'
        cls.revision_id = '8fefa9b6-56fa-e811-a995-a3d452a1c2f6'
        cls.index_field_id = '46c4f665-56fa-e811-a9cf-8b72d90dd505'
        cls.index_field_name = 'test'
        cls.folder_id = '75cb5823-50fa-e811-a995-a3d452a1c2f6'

    def test_get_documents(self):
        """
        tests Document.get_documents
        """
        document_service = Document(self.vault)
        resp = document_service.get_documents(self.query_string)
        self.assertEqual(resp['meta']['status'], 200)
        documents = resp['data']
        self.assertGreater(len(documents), 0)
        for document in documents:
            self.assertEqual(document['folderPath'], self.folder_path)

    def test_get_document(self):
        """
        tests Document.get_document
        """
        document_service = Document(self.vault)
        resp = document_service.get_document(self.document_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)

    def test_get_document_revisions(self):
        """
        tests Document.get_document_revisions
        """
        document_service = Document(self.vault)
        resp = document_service.get_document_revisions(self.document_id)
        self.assertEqual(resp['meta']['status'], 200)
        documents = resp['data']
        self.assertGreater(len(documents), 0)
        for document in documents:
            self.assertEqual(document['documentId'], self.document_id)

    def test_get_document_revision(self):
        """
        tests Document.get_document_revision
        """
        document_service = Document(self.vault)
        resp = document_service.get_document_revision(self.document_id, self.revision_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['id'], self.revision_id)
        self.assertEqual(resp['data']['documentId'], self.document_id)

    def test_get_document_index_fields(self):
        """
        tests Document.get_document_index_fields
        """
        document_service = Document(self.vault)
        resp = document_service.get_document_index_fields(self.document_id)
        self.assertEqual(resp['meta']['status'], 200)
        index_fields = resp['data']
        self.assertGreater(len(index_fields), 0)
        for index_field in index_fields:
            self.assertEqual(index_field['dataType'], 'DocumentIndexField')

    def test_get_document_index_field(self):
        """
        tests Document.get_document_index_field
        """
        document_service = Document(self.vault)
        resp = document_service.get_document_index_field(self.document_id, self.index_field_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['fieldId'], self.index_field_id)

    def test_get_document_revision_index_fields(self):
        """
        tests Document.get_document_revision_index_fields
        """
        document_service = Document(self.vault)
        resp = document_service.get_document_revision_index_fields(self.document_id, self.revision_id)
        self.assertEqual(resp['meta']['status'], 200)
        index_fields = resp['data']
        self.assertGreater(len(index_fields), 0)
        for index_field in index_fields:
            self.assertEqual(index_field['fieldId'], self.index_field_id)

    def test_get_document_revision_index_field(self):
        """
        tests Document.get_document_revision_index_field
        """
        document_service = Document(self.vault)
        resp = document_service.get_document_revision_index_field(self.document_id, self.revision_id, self.index_field_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['fieldId'], self.index_field_id)

    def test_update_document_index_fields(self):
        """
        tests Document.update_document_index_fields
        """
        document_service = Document(self.vault)
        expected_value = generate_random_uuid()
        fields_dict = str({self.index_field_name: expected_value})
        resp = document_service.update_document_index_fields(self.document_id, fields_dict)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['fieldId'], self.index_field_id)
        # self.assertEqual(resp['data'][0]['value'], expected_value)  # TODO: uncomment when API resolves bug
        new_value = document_service.get_document_index_field(self.document_id, self.index_field_id)['data']['value']
        self.assertEqual(new_value, expected_value)

    def test_update_document_index_field(self):
        """
        tests Document.update_document_index_field
        """
        document_service = Document(self.vault)
        expected_value = generate_random_uuid()
        resp = document_service.update_document_index_field(self.document_id, self.index_field_id, expected_value)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['fieldId'], self.index_field_id)
        self.assertEqual(resp['data']['value'], expected_value)
        new_value = document_service.get_document_index_field(self.document_id, self.index_field_id)['data']['value']
        self.assertEqual(new_value, expected_value)

    def test_new_document_and_delete_document(self):
        """
        tests Document.new_document and Document.delete_document
        """
        document_service = Document(self.vault)

        # new document
        resp = document_service.new_document(self.folder_id, 1, '_test_doc', '_test_doc description', '0', '_test.txt')
        self.assertEqual(resp['meta']['status'], 200)
        document_id = resp['data']['documentId']
        revision_id = resp['data']['id']

        # validate document exists in VV
        resp = document_service.get_document(document_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], document_id)

        # delete document
        resp = document_service.delete_document(revision_id)  # TODO: possibly update API docs
        self.assertEqual(resp['meta']['status'], 200)

        # validate document does not exist in VV
        # resp = document_service.get_document(document_id)
        # self.assertEqual(resp['meta']['status'], 404)  # TODO: review with Tod
