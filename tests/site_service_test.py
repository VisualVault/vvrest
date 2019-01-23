import unittest
from .utilities import get_vault_object, generate_random_uuid, get_parameters_json
from vvrest.services.site_service import SiteService


class SiteServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()
        test_parameters = get_parameters_json()
        cls.site_id = test_parameters['site_id']
        cls.group_id = test_parameters['group_id']
        cls.user_id = test_parameters['user_id']

    def test_get_sites(self):
        """
        tests SiteService.get_sites
        """
        site_service = SiteService(self.vault)
        resp = site_service.get_sites()

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        self.assertEqual(resp['data'][0]['dataType'], 'Site')

    def test_get_site(self):
        """
        tests SiteService.get_site
        """
        site_service = SiteService(self.vault)
        resp = site_service.get_site(self.site_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(len(resp['data']), 1)  # TODO: report return list instead of object
        self.assertEqual(resp['data'][0]['dataType'], 'Site')
        self.assertEqual(resp['data'][0]['id'], self.site_id)

    def test_get_site_users(self):
        """
        tests SiteService.get_site_users
        """
        site_service = SiteService(self.vault)
        resp = site_service.get_site_users(self.site_id)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertGreater(len(resp['data']), 0)
        for user in resp['data']:
            self.assertEqual(user['dataType'], 'User')
            self.assertEqual(user['siteId'], self.site_id)

    def test_create_site(self):
        """
        tests SiteService.create_site
        """
        site_service = SiteService(self.vault)

        # create site
        expected_site_name = generate_random_uuid()
        expected_site_description = expected_site_name + ' description'
        resp = site_service.create_site(expected_site_name, expected_site_description)

        # validate site
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['dataType'], 'Site')
        self.assertEqual(resp['data']['name'], expected_site_name)
        self.assertEqual(resp['data']['description'], expected_site_description)
        site_id = resp['data']['id']

        # validate newly created site
        resp = site_service.get_site(site_id)
        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data'][0]['dataType'], 'Site')  # TODO: report return list instead of object
        self.assertEqual(resp['data'][0]['id'], site_id)
        self.assertEqual(resp['data'][0]['name'], expected_site_name)
        self.assertEqual(resp['data'][0]['description'], expected_site_description)
