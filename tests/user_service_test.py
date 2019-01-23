import unittest
from .utilities import get_vault_object, generate_random_uuid, get_parameters_json
from vvrest.services.user_service import UserService
from uuid import UUID


class UserServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()
        test_parameters = get_parameters_json()
        cls.site_id = test_parameters['site_id']
        cls.user_id = test_parameters['user_id']

    def test_get_users(self):
        """
        tests UserService.get_users
        """
        user_service = UserService(self.vault)
        resp = user_service.get_users()

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        for user in resp['data']:
            self.assertEqual(user['dataType'], 'User')

    def test_get_user(self):
        """
        tests UserService.get_user
        """
        user_service = UserService(self.vault)
        resp = user_service.get_user(self.user_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['id'], self.user_id)
        self.assertEqual(resp['data']['dataType'], 'User')

    def test_get_user_web_token(self):
        """
        tests UserService.get_user_web_token
        """
        user_service = UserService(self.vault)
        resp = user_service.get_user_web_token(self.user_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertIn('webToken', resp['data'])
        UUID(resp['data']['webToken'], version=4)  # validate webToken is a valid uuid4

    def test_update_user(self):
        """
        tests UserService.update_user
        """
        user_service = UserService(self.vault)

        # get user
        initial_last_name = user_service.get_user(self.user_id)['data']['lastName']
        expected_last_name = generate_random_uuid()
        self.assertNotEqual(initial_last_name, expected_last_name)

        # update user last name
        resp = user_service.update_user(self.user_id, dict(lastName=expected_last_name))
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['id'], self.user_id)
        self.assertEqual(resp['data']['dataType'], 'User')
        self.assertEqual(resp['data']['lastName'], expected_last_name)

        # validate updated user
        resp = user_service.get_user(self.user_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['id'], self.user_id)
        self.assertEqual(resp['data']['dataType'], 'User')
        self.assertEqual(resp['data']['lastName'], expected_last_name)
