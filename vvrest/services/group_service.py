import requests
from ..constants import GROUPS_URL, USERS_URL


class GroupService:
	def __init__(self, vault):
		self.vault = vault

	def get_groups(self, query=''):
		"""
		get all groups or search by query
		:param query: string, example: TODO: query example
		:return: dict
		"""
		request_url = self.vault.base_url + GROUPS_URL
		if query:
			request_url += '?q=' + query

		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def get_group(self, group_id):
		"""
		get a group by id
		:param group_id: string uuid4
		:return: dict
		"""
		endpoint = GROUPS_URL + '/' + group_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def get_group_users(self, group_id):
		"""
		get users of a group by id
		:param group_id: string uuid4
		:return: dict
		"""
		endpoint = GROUPS_URL + '/' + group_id + '/' + USERS_URL
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def get_group_user(self, group_id, user_id):
		"""
		get a user of a group by ids
		:param group_id: string uuid4
		:param user_id: string uuid4
		:return: dict
		"""
		endpoint = GROUPS_URL + '/' + group_id + '/' + USERS_URL + '/' + user_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def create_group(self, name, description, site_id):
		"""
		create a new group
		:param name: string
		:param description: string
		:param site_id: string uuid4
		:return: dict
		"""
		request_url = self.vault.base_url + GROUPS_URL
		headers = self.vault.get_auth_headers()

		payload = {
			'name': name,
			'description': description,
			'siteId': site_id
		}

		resp = requests.post(request_url, data=payload, headers=headers).json()

		return resp

	def update_group(self, group_id, name, description):
		"""
		create a new group
		:param group_id: string uuid4
		:param name: string
		:param description: string
		:return: dict
		"""
		endpoint = GROUPS_URL + '/' + group_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()

		payload = {
			'name': name,
			'description': description
		}

		resp = requests.put(request_url, data=payload, headers=headers).json()

		return resp

	def add_user_to_group(self, group_id, user_id):
		"""
		adds a user to a group
		:param group_id: string uuid4
		:param user_id: string uuid4
		:return: dict
		"""
		endpoint = GROUPS_URL + '/' + group_id + '/' + USERS_URL + '/' + user_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.put(request_url, headers=headers).json()

		return resp
