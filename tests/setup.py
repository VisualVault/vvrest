import os
import json
import unittest
from .utilities import get_vault_object, generate_random_uuid, get_parameters_json
from vvrest.services.document_service import DocumentService
from vvrest.services.folder_service import FolderService
from vvrest.services.index_field_service import IndexFieldService
from vvrest.services.site_service import SiteService
from vvrest.services.group_service import GroupService
from vvrest.services.user_service import UserService


class SetupTestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()
        cls.test_parameters = os.getcwd() + '/tests/parameters.json'

    def test_setup_test_suite(self):
        """
        updates parameters.json for VVRestTestSuite
        """
        document_service = DocumentService(self.vault)
        folder_service = FolderService(self.vault)
        index_field_service = IndexFieldService(self.vault)
        site_service = SiteService(self.vault)
        group_service = GroupService(self.vault)
        user_service = UserService(self.vault)

        # create folder
        expected_folder_name = generate_random_uuid()
        expected_folder_description = expected_folder_name + ' description'
        resp = folder_service.new_folder(expected_folder_name, expected_folder_description, True)
        folder_id = resp['data']['id']
        folder_path = '/' + expected_folder_name
        query_string = "folderPath='" + folder_path + "'"

        # create sub folder
        expected_sub_folder_name = generate_random_uuid()
        expected_sub_folder_description = expected_sub_folder_name + ' description'
        resp = folder_service.new_sub_folder(folder_id, expected_sub_folder_name, expected_sub_folder_description, True)
        self.assertEqual(resp['meta']['status'], 200)
        sub_folder_id = resp['data']['id']
        sub_folder_path = folder_path + '/' + expected_sub_folder_name

        # create index field definition
        expected_label = generate_random_uuid()
        expected_description = expected_label + ' description'
        resp = index_field_service.create_index_field(expected_label, expected_description, 1, True, 'DEFAULT')
        self.assertEqual(resp['meta']['status'], 200)
        index_field_id = resp['data']['id']
        index_field_name = expected_label

        # relate index field definition to folder
        resp = index_field_service.relate_index_field_to_folder(index_field_id, folder_id)
        self.assertEqual(resp['meta']['status'], 200)

        # create document
        resp = document_service.new_document(folder_id, 1, '_test_doc', '_test_doc description', '0', '_test.txt')
        self.assertEqual(resp['meta']['status'], 200)
        document_id = resp['data']['documentId']
        document_revision_id = resp['data']['id']

        # create site
        expected_site_name = generate_random_uuid()
        expected_site_description = expected_site_name + ' description'
        resp = site_service.create_site(expected_site_name, expected_site_description)
        self.assertEqual(resp['meta']['status'], 200)
        site_id = resp['data']['id']

        # create new group
        expected_group_name = generate_random_uuid()
        expected_group_description = expected_group_name + ' description'
        resp = group_service.create_group(expected_group_name, expected_group_description, site_id)
        self.assertEqual(resp['meta']['status'], 200)
        group_id = resp['data']['id']

        # create user
        user_id = generate_random_uuid()
        first_name = 'test'
        last_name = 'test'
        email = 'test@visualvault.com'
        password = 'TsT3!aB4@sY7'
        resp = user_service.create_user(site_id, user_id, first_name, last_name, email, password)
        self.assertEqual(resp['meta']['status'], 200)
        user_id = resp['data']['id']

        # add user to group
        resp = group_service.add_user_to_group(group_id, user_id)
        self.assertEqual(resp['meta']['status'], 201)

        # setup test_parameters json
        if os.path.isfile(self.test_parameters):
            parameters = get_parameters_json()
            parameters['folder_path'] = folder_path
            parameters['query_string'] = query_string
            parameters['document_id'] = document_id
            parameters['document_revision_id'] = document_revision_id
            parameters['index_field_id'] = index_field_id
            parameters['index_field_name'] = index_field_name
            parameters['folder_id'] = folder_id
            parameters['folder_name'] = expected_folder_name
            parameters['sub_folder_id'] = sub_folder_id
            parameters['sub_folder_path'] = sub_folder_path
            parameters['site_id'] = site_id
            parameters['group_id'] = group_id
            parameters['user_id'] = user_id
        else:
            parameters = dict(
                folder_path=folder_path,
                query_string=query_string,
                document_id=document_id,
                document_revision_id=document_revision_id,
                index_field_id=index_field_id,
                index_field_name=index_field_name,
                folder_id=folder_id,
                folder_name=expected_folder_name,
                sub_folder_id=sub_folder_id,
                sub_folder_path=sub_folder_path,
                site_id=site_id,
                group_id=group_id,
                user_id=user_id
            )

        with open(self.test_parameters, 'w+') as parameters_file:
            json.dump(parameters, parameters_file)  # write test_parameters to parameters.json
