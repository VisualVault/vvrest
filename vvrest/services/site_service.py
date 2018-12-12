import requests
from ..constants import SITES_URL, USERS_URL


class SiteService:
    def __init__(self, vault):
        self.vault = vault

    def get_sites(self):
        """
        get all sites
        :return: dict
        """
        request_url = self.vault.base_url + SITES_URL
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_site(self, site_id):
        """
        get a site by id
        :param site_id: string uuid4
        :return: dict
        """
        endpoint = SITES_URL + '/' + site_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_site_users(self, site_id):
        """
        get all users of a site
        :param site_id: string uuid4
        :return: dict
        """
        endpoint = SITES_URL + '/' + site_id + '/' + USERS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def create_site(self, name, description):
        """
        create a new site
        :param name: string
        :param description: string
        :return: dict
        """
        request_url = self.vault.base_url + SITES_URL
        headers = self.vault.get_auth_headers()

        payload = {
            'name': name,
            'description': description
        }

        resp = requests.post(request_url, headers=headers, data=payload).json()

        return resp

    def create_site_user(self, site_id, user_id, first_name, last_name, email, password):
        """
        creates a new user for a site TODO: add name, write unit test, report possible bug
        :param site_id: string uuid4
        :param user_id: string uuid4
        :param first_name: string
        :param last_name: string
        :param email: string
        :param password: string
        :return: dict
        """
        endpoint = SITES_URL + '/' + site_id + '/' + USERS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()

        payload = {
            'userId': user_id,
            'firstName': first_name,
            'lastName': last_name,
            'email': email,
            'password': password
        }

        resp = requests.post(request_url, headers=headers, data=payload).json()

        return resp
