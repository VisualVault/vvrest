import requests
from ..constants import FORM_TEMPLATES_URL, FORMS_URL, PDF_URL, FIELDS_URL, FORM_INSTANCE_URL, RELATE_FORM_URL, \
						RELATE_DOCUMENT_URL, RELATE_PROJECT_URL, UNRELATE_FORM_URL, UNRELATE_DOCUMENT_URL, \
						UNRELATE_PROJECT_URL, VV_LOGIN_URL, RETURN_URL, HIDE_MENU_URL, DOCUMENTS_URL


class FormService:
	def __init__(self, vault):
		self.vault = vault

	def get_form_templates(self, query=''):
		"""
		get all form templates or search by query string
		:param query: string, example: "name='TestForm'"
		:return: dict
		"""
		request_url = self.vault.base_url + FORM_TEMPLATES_URL

		# check for query string parameter
		if query:
			request_url += '?q=' + query

		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def get_form_template(self, template_id):
		"""
		get a form template by id
		:param template_id: string uuid4
		:return: dict
		"""
		endpoint = FORM_TEMPLATES_URL + '/' + template_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def get_form_instance(self, template_id, instance_id, query_string=''):
		"""
		get a form instance by form template and instance ids
		:param template_id: string uuid4
		:param instance_id: string uuid4
		:param query_string: string, example: 'fields=Signature,TestField'
		:return: dict
		"""
		endpoint = FORM_TEMPLATES_URL + '/' + template_id + '/' + FORMS_URL + '/' + instance_id

		if query_string:
			endpoint += '?' + query_string

		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def form_instance_pdf_download(self, template_id, instance_id, file_path):
		"""
		downloads a form instance as a PDF to the passed in file_path
		:param template_id: string uuid4
		:param instance_id: string uuid4
		:param file_path: string, example: /test_dir/test_file.pdf
		:return: None
		"""
		endpoint = FORM_TEMPLATES_URL + '/' + template_id + '/' + FORMS_URL + '/' + instance_id + '/' + PDF_URL
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		stream = requests.get(request_url, headers=headers, stream=True)

		with open(file_path, 'wb') as file:
			data = stream.raw.read()
			file.write(data)

	def get_form_template_fields(self, template_id):
		"""
		get form fields for a form template
		:param template_id: string uuid4
		:return: dict
		"""
		endpoint = FORM_TEMPLATES_URL + '/' + template_id + '/' + FIELDS_URL
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def get_form_instances(self, template_id, query_string=''):
		"""
		get all form instances for a form template
		:param template_id: string uuid4
		:param query_string: string, example: 'fields=DocumentType'
		:return: dict
		"""
		endpoint = FORM_TEMPLATES_URL + '/' + template_id + '/' + FORMS_URL

		if query_string:
			endpoint += '?' + query_string

		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def get_form_instances_search(self, template_id, query):
		"""
		get all form instances for a form template
		:param template_id: string uuid4
		:param query: string, example: "instanceName='testForm-000026'&fields=field1,field2"
		:return: dict
		"""
		endpoint = FORM_TEMPLATES_URL + '/' + template_id + '/' + FORMS_URL + '?q=' + query
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def create_form_instance(self, template_id, fields_dict):
		"""
		create a form instance of a form template
		by filling out a form with the provided fields_dict
		:param template_id: string uuid4
		:param fields_dict: dict, example: {'field1': '5', 'field2': True, 'field3': 5}
		:return: dict
		"""
		endpoint = FORM_TEMPLATES_URL + '/' + template_id + '/' + FORMS_URL
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.post(request_url, headers=headers, data=fields_dict).json()

		return resp

	def create_form_instance_revision(self, template_id, instance_id, fields_dict):
		"""
		create a form instance revision of a form template
		by filling out a form with the provided fields_dict
		:param template_id: string uuid4
		:param instance_id: sting uuid4
		:param fields_dict: dict, example: {'field1': '5', 'field2': True, 'field3': 5}
		:return: dict
		"""
		endpoint = FORM_TEMPLATES_URL + '/' + template_id + '/' + FORMS_URL + '/' + instance_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.post(request_url, headers=headers, data=fields_dict).json()

		return resp

	def relate_form(self, instance_id1, instance_id2):
		"""
		relate a form instance to another form instance
		:param instance_id1: string uuid4
		:param instance_id2: string uuid4
		:return: dict
		"""
		endpoint = FORM_INSTANCE_URL + '/' + instance_id1 + '/' + RELATE_FORM_URL + instance_id2
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.put(request_url, headers=headers).json()

		return resp

	def relate_document(self, instance_id, document_id):
		"""
		relate a form instance to a document
		:param instance_id: string uuid4
		:param document_id: string uuid4
		:return: dict
		"""
		endpoint = FORM_INSTANCE_URL + '/' + instance_id + '/' + RELATE_DOCUMENT_URL + document_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.put(request_url, headers=headers).json()

		return resp

	def relate_project(self, instance_id, project_id):
		"""
		relate a form instance to a project
		:param instance_id: string uuid4
		:param project_id: string uuid4
		:return: dict
		"""
		endpoint = FORM_INSTANCE_URL + '/' + instance_id + '/' + RELATE_PROJECT_URL + project_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.put(request_url, headers=headers).json()

		return resp

	def unrelate_form(self, instance_id1, instance_id2):
		"""
		unrelate a form instance to another form instance
		:param instance_id1: string uuid4
		:param instance_id2: string uuid4
		:return: dict
		"""
		endpoint = FORM_INSTANCE_URL + '/' + instance_id1 + '/' + UNRELATE_FORM_URL + instance_id2
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.put(request_url, headers=headers).json()

		return resp

	def unrelate_document(self, instance_id, document_id):
		"""
		unrelate a form instance to a document
		:param instance_id: string uuid4
		:param document_id: string uuid4
		:return: dict
		"""
		endpoint = FORM_INSTANCE_URL + '/' + instance_id + '/' + UNRELATE_DOCUMENT_URL + document_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.put(request_url, headers=headers).json()

		return resp

	def unrelate_project(self, instance_id, project_id):
		"""
		unrelate a form instance to a project
		:param instance_id: string uuid4
		:param project_id: string uuid4
		:return: dict
		"""
		endpoint = FORM_INSTANCE_URL + '/' + instance_id + '/' + UNRELATE_PROJECT_URL + project_id
		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.put(request_url, headers=headers).json()

		return resp

	def get_embedded_form(self, web_token, instance_id):
		"""
		returns a url that can be embedded in an i-frame that will launch a form instance
		:param web_token: string uuid4, example: web_token returned from UserService.get_user_web_token
		:param instance_id: string uuid4
		:return: string
		"""
		login_url = self.vault.url + '/' + VV_LOGIN_URL + web_token  # authentication portion of form url
		return_url = RETURN_URL + instance_id + HIDE_MENU_URL  # form instance portion of form url
		form_url = login_url + return_url

		return form_url

	def get_related_documents(self, instance_id, query_string=''):
		"""
		get related documents of a form instance
		:param instance_id: string uuid4
		:param query_string: string, example: 'indexFields=include'
		:return: dict
		"""
		endpoint = FORM_INSTANCE_URL + '/' + instance_id + '/' + DOCUMENTS_URL

		if query_string:
			endpoint += '?' + query_string

		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp

	def get_related_forms(self, instance_id, query_string=''):
		"""
		get related forms of a form instance
		:param instance_id: string uuid4
		:param query_string: string, example: "q=[instanceName]='TEST-00000064'"
		:return: dict
		"""
		endpoint = FORM_INSTANCE_URL + '/' + instance_id + '/' + FORMS_URL

		if query_string:
			endpoint += '?' + query_string

		request_url = self.vault.base_url + endpoint
		headers = self.vault.get_auth_headers()
		resp = requests.get(request_url, headers=headers).json()

		return resp
