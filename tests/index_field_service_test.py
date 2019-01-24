import unittest
from .utilities import get_vault_object, generate_random_uuid, get_parameters_json
from vvrest.services.index_field_service import IndexFieldService


class IndexFieldServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
            cls.vault = get_vault_object()

        test_parameters = get_parameters_json()
        cls.index_field_id = test_parameters['index_field_id']
        cls.folder_id = test_parameters['folder_id']

    def test_get_index_fields(self):
        """
        tests IndexFieldService.get_index_fields
        """
        index_field_service = IndexFieldService(self.vault)
        resp = index_field_service.get_index_fields()
        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)

    def test_create_and_update_index_field(self):
        """
        tests IndexFieldService.create_index_field, IndexFieldService.update_index_field,
        and IndexFieldService.relate_index_field_to_folder
        """
        index_field_service = IndexFieldService(self.vault)

        expected_label = generate_random_uuid()
        expected_description = expected_label + ' description'

        # create new index field definition
        resp = index_field_service.create_index_field(expected_label, expected_description, 1, True, 'DEFAULT')
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['dataType'], 'IndexFieldDefinition')
        self.assertEqual(resp['data']['label'], expected_label)
        self.assertEqual(resp['data']['description'], expected_description)
        index_field_id = resp['data']['id']

        # validate new index field
        resp = index_field_service.get_index_fields(query="label='" + expected_label + "'")
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['dataType'], 'IndexFieldDefinition')
        self.assertEqual(resp['data'][0]['label'], expected_label)
        self.assertEqual(resp['data'][0]['description'], expected_description)

        updated_expected_label = generate_random_uuid()
        updated_expected_description = updated_expected_label
        self.assertNotEqual(expected_label, updated_expected_label)

        # update index field definition
        resp = index_field_service.update_index_field(index_field_id, updated_expected_label, updated_expected_description, 1, True, 'DEFAULT')
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['dataType'], 'IndexFieldDefinition')
        self.assertEqual(resp['data']['label'], updated_expected_label)
        self.assertEqual(resp['data']['description'], updated_expected_description)

        # get updated index_field
        resp = index_field_service.get_index_fields(query="label='" + updated_expected_label + "'")
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)
        self.assertEqual(resp['data'][0]['dataType'], 'IndexFieldDefinition')
        self.assertEqual(resp['data'][0]['label'], updated_expected_label)
        self.assertEqual(resp['data'][0]['description'], updated_expected_description)

        # relate new index field to folder
        resp = index_field_service.relate_index_field_to_folder(index_field_id, self.folder_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['folderId'], self.folder_id)
        self.assertEqual(resp['data']['dataType'], 'FolderIndexField')
        self.assertEqual(resp['data']['id'], index_field_id)
