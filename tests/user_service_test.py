import unittest
from .utilities import get_vault_object, generate_random_uuid, get_parameters_json
from vvrest.services.user_service import UserService
from uuid import UUID


class UserServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
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
        user_web_token = resp['data']['webToken']
        UUID(user_web_token, version=4)  # validate webToken is a valid uuid4

        # validate user impersonation
        vault_impersonation = get_vault_object(user_web_token)
        user_service = UserService(vault_impersonation)
        resp = user_service.get_users()

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        for user in resp['data']:
            self.assertEqual(user['dataType'], 'User')

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

    def test_create_user(self):
        """
        tests UserService.create_user
        """
        user_service = UserService(self.vault)

        # set fields
        expected_user_id = generate_random_uuid()
        first_name = 'test'
        last_name = 'test'
        email = 'test@visualvault.com'
        password = 'TsT3!aB4@sY7'

        resp = user_service.create_user(self.site_id, expected_user_id, first_name, last_name, email, password)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['dataType'], 'User')
        self.assertEqual(resp['data']['name'], expected_user_id)

    def test_get_user_jwt(self):
        user_service = UserService(self.vault)

        resp = user_service.get_user_jwt()
        self.assertEqual(resp['meta']['status'], 200)
        self.assertIn('token', resp['data'])
        self.assertIn('expires', resp['data'])
