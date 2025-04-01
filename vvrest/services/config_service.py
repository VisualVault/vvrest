import requests

from ..constants import CONFIG_URL, DOCAPI_URL


class ConfigService:
	def __init__(self, vault):
		self.vault = vault

	def get_docapi_config(self):
		"""
		get docapi config info
		:return: dict
		"""
		request_url = self.vault.base_url + CONFIG_URL + '/' + DOCAPI_URL
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp
