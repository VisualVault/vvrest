import requests
from ..constants import DOCUMENTS_URL, REVISIONS_URL, INDEX_FIELDS_URL


class DocumentService:
    def __init__(self, vault):
        """
        :param vault: Vault
        """
        self.vault = vault

    def get_documents(self, query_string):
        """
        get documents by query string parameter
        :param query_string: string, example: "folderPath='/test'"
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '?q=' + query_string
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_document(self, document_id):
        """
        get document by documentId
        :param document_id: string uuid4
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_document_revisions(self, document_id):
        """
        get revisions of a document by documentId
        :param document_id: string uuid4
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id + '/' + REVISIONS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_document_revision(self, document_id, revision_id):
        """
        get a specific revision of a document by documentId and revisionId
        :param document_id: string uuid4
        :param revision_id: string uuid4
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id + '/' + REVISIONS_URL + '/' + revision_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_document_index_fields(self, document_id):
        """
        get indexfields for a document
        :param document_id: string uuid4
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id + '/' + INDEX_FIELDS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_document_index_field(self, document_id, field_id):
        """
        get a document index field by documentId and fieldId
        :param document_id: string uuid4
        :param field_id: string uuid4
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id + '/' + INDEX_FIELDS_URL + '/' + field_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_document_revision_index_fields(self, document_id, revision_id):
        """
        get index fields for a document revision
        :param document_id: string uuid4
        :param revision_id: string uuid4
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id + '/' + REVISIONS_URL + '/' + revision_id + '/' + INDEX_FIELDS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_document_revision_index_field(self, document_id, revision_id, field_id):
        """
        get a index field of a revision of a document by documentId and revisionId
        :param document_id: string uuid4
        :param revision_id: string uuid4
        :param field_id: string uuid4
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id + '/' + REVISIONS_URL + '/' + revision_id + '/' + INDEX_FIELDS_URL + '/' + field_id

        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def update_document_index_fields(self, document_id, fields_dict):
        """
        update one to many document index fields
        :param document_id: string uuid4
        :param fields_dict: string dict, example: "{'test': 'changed value'}"
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id + '/' + INDEX_FIELDS_URL
        request_url = self.vault.base_url + endpoint
        fields = {'indexfields': fields_dict}
        headers = self.vault.get_auth_headers()
        resp = requests.put(request_url, headers=headers, data=fields).json()

        return resp

    def update_document_index_field(self, document_id, field_id, value):
        """
        updates a document index field
        :param document_id: string uuid4
        :param field_id: string uuid4
        :param value: string
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id + '/' + INDEX_FIELDS_URL + '/' + field_id
        request_url = self.vault.base_url + endpoint
        fields = {'value': value}
        headers = self.vault.get_auth_headers()
        resp = requests.put(request_url, headers=headers, data=fields).json()

        return resp

    def new_document(self, folder_id, document_state, name, description, revision, file_name):
        """
        creates a document object with no file attached. first step in file upload process.
        :param folder_id: string uuid4
        :param document_state: int
        :param name: string
        :param description: string
        :param revision: string
        :param file_name: string
        :return:
        """
        endpoint = DOCUMENTS_URL
        request_url = self.vault.base_url + endpoint

        payload = {
            'folderId': folder_id,
            'documentState': document_state,
            'name': name,
            'description': description,
            'revision': revision,
            'allowNoFile': True,
            'fileLength': 0,
            'fileName': file_name,
            'indexFields': '{}'
        }

        headers = self.vault.get_auth_headers()
        resp = requests.post(request_url, data=payload, headers=headers).json()

        return resp

    def delete_document(self, document_id):
        """
        :param document_id: string uuid4
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + document_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.delete(request_url, headers=headers).json()

        return resp
