import unittest
from .utilities import get_vault_object, generate_random_uuid
from vvrest.services.folder_service import FolderService


class FolderServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()
        cls.folder_name = 'test'
        cls.folder_path = '/test'
        cls.folder_id = '75cb5823-50fa-e811-a995-a3d452a1c2f6'
        cls.sub_folder_id = '80bfeff9-96fc-e811-a995-a3d452a1c2f6'
        cls.sub_folder_path = '/test/sub_test'
        cls.document_id = '810013e6-50fa-e811-a9cf-8b72d90dd505'
        cls.index_field_id = '46c4f665-56fa-e811-a9cf-8b72d90dd505'

    def test_get_folder_search(self):
        """
        tests FolderService.get_folder_search
        """
        folder_service = FolderService(self.vault)
        resp = folder_service.get_folder_search(self.folder_name)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['id'], self.folder_id)
        self.assertEqual(resp['data']['folderPath'], self.folder_path)

    def test_get_folder(self):
        """
        tests FolderService.get_folder
        """
        folder_service = FolderService(self.vault)
        resp = folder_service.get_folder(self.folder_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['id'], self.folder_id)
        self.assertEqual(resp['data']['folderPath'], self.folder_path)

    def test_get_sub_folders(self):
        """
        tests FolderService.get_sub_folders
        """
        folder_service = FolderService(self.vault)
        resp = folder_service.get_sub_folders(self.folder_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['id'], self.sub_folder_id)
        self.assertEqual(resp['data'][0]['folderPath'], self.sub_folder_path)

    def test_get_folder_documents(self):
        """
        tests FolderService.get_folder_documents
        """
        folder_service = FolderService(self.vault)
        resp = folder_service.get_folder_documents(self.folder_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['documentId'], self.document_id)
        self.assertEqual(resp['data'][0]['folderPath'], self.folder_path)

    def test_get_folder_index_fields(self):
        """
        tests FolderService.get_folder_index_fields
        """
        folder_service = FolderService(self.vault)
        resp = folder_service.get_folder_index_fields(self.folder_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['id'], self.index_field_id)

    def test_get_folder_index_field(self):
        """
        tests FolderService.get_folder_index_field
        """
        folder_service = FolderService(self.vault)
        resp = folder_service.get_folder_index_field(self.folder_id, self.index_field_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['id'], self.index_field_id)

    def test_new_folder_and_new_sub_folder(self):
        """
        tests FolderService.new_folder and FolderService.new_sub_folder
        """
        folder_service = FolderService(self.vault)
        expected_folder_name = generate_random_uuid()
        expected_folder_description = expected_folder_name + ' description'
        resp = folder_service.new_folder(expected_folder_name, expected_folder_description, True)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['name'], expected_folder_name)
        self.assertEqual(resp['data']['folderPath'], '/' + expected_folder_name)
        self.assertEqual(resp['data']['description'], expected_folder_description)

        folder_id = resp['data']['id']
        expected_sub_folder_name = generate_random_uuid()
        expected_sub_folder_description = expected_sub_folder_name + ' description'
        resp = folder_service.new_sub_folder(folder_id, expected_sub_folder_name, expected_sub_folder_description, True)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['name'], expected_sub_folder_name)
        self.assertEqual(resp['data']['folderPath'], '/' + expected_folder_name + '/' + expected_sub_folder_name)
        self.assertEqual(resp['data']['description'], expected_sub_folder_description)

    def test_update_folder_index_field(self):
        """
        tests FolderService.update_folder_index_field
        """
        folder_service = FolderService(self.vault)

        # get original index_field default value
        original_index_field_value = folder_service.get_folder_index_field(self.folder_id, self.index_field_id)['data']['defaultValue']

        # generate new index_field default value
        expected_index_field_value = generate_random_uuid()
        self.assertNotEqual(original_index_field_value, expected_index_field_value)
        resp = folder_service.update_folder_index_field(self.folder_id, self.index_field_id, False, expected_index_field_value)

        # validate index_field default value has changed
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['id'], self.index_field_id)
        self.assertEqual(resp['data']['defaultValue'], expected_index_field_value)

        # fetch index_field and validate default value has changed
        new_index_field_value = folder_service.get_folder_index_field(self.folder_id, self.index_field_id)['data']['defaultValue']
        self.assertEqual(new_index_field_value, expected_index_field_value)
