import unittest
from .utilities import get_vault_object, generate_random_uuid, get_parameters_json
from vvrest.services.group_service import GroupService


class GroupServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
            cls.vault = get_vault_object()

        test_parameters = get_parameters_json()
        cls.site_id = test_parameters['site_id']
        cls.group_id = test_parameters['group_id']
        cls.user_id = test_parameters['user_id']

    def test_get_groups(self):
        """
        tests GroupService.get_groups
        """
        group_service = GroupService(self.vault)
        resp = group_service.get_groups()

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        self.assertEqual(resp['data'][0]['dataType'], 'Group')

    def test_get_group(self):
        """
        tests GroupService.get_group
        """
        group_service = GroupService(self.vault)
        resp = group_service.get_group(self.group_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)  # TODO: report returns list instead of object
        self.assertEqual(resp['data'][0]['dataType'], 'Group')
        self.assertEqual(resp['data'][0]['id'], self.group_id)

    def test_get_group_users(self):
        """
        tests GroupService.get_group_users
        """
        group_service = GroupService(self.vault)
        resp = group_service.get_group_users(self.group_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        self.assertEqual(resp['data'][0]['dataType'], 'User')

    def test_get_group_user(self):
        """
        tests GroupService.get_group_user
        """
        group_service = GroupService(self.vault)
        resp = group_service.get_group_user(self.group_id, self.user_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['dataType'], 'User')
        self.assertEqual(resp['data']['id'], self.user_id)

    def test_create_and_update_group(self):
        """
        tests GroupService.create_group, GroupService.update_group, and GroupService.add_user_to_group
        """
        group_service = GroupService(self.vault)

        # create new group
        expected_group_name = generate_random_uuid()
        expected_group_description = expected_group_name + ' description'
        resp = group_service.create_group(expected_group_name, expected_group_description, self.site_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['dataType'], 'Group')
        self.assertEqual(resp['data']['name'], expected_group_name)
        self.assertEqual(resp['data']['description'], expected_group_description)

        group_id = resp['data']['id']
        expected_group_name = generate_random_uuid()
        expected_group_description = expected_group_name + ' description'

        # update group
        resp = group_service.update_group(group_id, expected_group_name, expected_group_description)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['dataType'], 'Group')
        self.assertEqual(resp['data']['name'], expected_group_name)
        self.assertEqual(resp['data']['description'], expected_group_description)

        # validate updated group data
        resp = group_service.get_group(group_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)  # TODO: report returns list instead of object
        self.assertEqual(resp['data'][0]['id'], group_id)
        self.assertEqual(resp['data'][0]['dataType'], 'Group')
        self.assertEqual(resp['data'][0]['name'], expected_group_name)
        self.assertEqual(resp['data'][0]['description'], expected_group_description)

        # validate user is not in newly created group
        resp = group_service.get_group_user(group_id, self.user_id)
        self.assertEqual(resp['meta']['status'], 404)

        # add user to group
        resp = group_service.add_user_to_group(group_id, self.user_id)
        self.assertEqual(resp['meta']['status'], 201)
        self.assertEqual(len(resp['data']), 1)  # TODO: report returns list instead of object
        self.assertEqual(resp['data'][0]['dataType'], 'NotifyUser')  # TODO: report dataType validation
        self.assertEqual(resp['data'][0]['id'], self.user_id)

        # validate user is now a member of new group
        resp = group_service.get_group_user(group_id, self.user_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['dataType'], 'User')
        self.assertEqual(resp['data']['id'], self.user_id)
