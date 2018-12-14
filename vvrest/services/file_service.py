import requests
from ..constants import FILES_URL


class FileService:
    def __init__(self, vault):
        """
        :param vault: Vault
        """
        self.vault = vault

    def get_file_stream(self, file_id):
        """
        request a file stream by file_id
        :param file_id: string uuid4
        :return: stream
        """
        endpoint = FILES_URL + '/' + file_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        stream = requests.get(request_url, headers=headers, stream=True)  # get file stream

        return stream

    def get_file_stream_by_search(self, query):
        """
        request a file stream by query
        :param query: string, example: "id='8fefa9b6-56fa-e811-a995-a3d452a1c2f6'"
        :return: stream
        """
        endpoint = FILES_URL + '?q=' + query
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        stream = requests.get(request_url, headers=headers, stream=True)  # get file stream

        return stream

    def file_upload(self, document_id, name, revision, change_reason, check_in_state, index_fields, file_name, file_path):
        """
        :param document_id: string uuid4
        :param name: string
        :param revision: string
        :param change_reason: string
        :param check_in_state: string
        :param index_fields: string dict, example: "{'testFIELD': 'the value'}"
        :param file_name: string
        :param file_path: string
        :return: dict
        """
        request_url = self.vault.base_url + FILES_URL
        headers = self.vault.get_auth_headers()

        params = {
            'documentId': document_id,
            'name': name,
            'revision': revision,
            'changeReason': change_reason,
            'checkInDocumentState': check_in_state,
            'indexFields': index_fields,
            'fileName': file_name
        }

        with open(file_path, 'rb') as file_stream:  # open file stream
            files = {'fileUpload': (file_name, file_stream, 'application/octet-stream')}
            resp = requests.post(request_url, headers=headers, data=params, files=files).json()

        return resp
