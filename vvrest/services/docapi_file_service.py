import requests

from ..constants import FILES_URL, REVISIONS_URL


class DocApiFileService:
    def __init__(self, vault):
        """
        :param vault: Vault
        """
        self.vault = vault
        
        # if docapi is not enabled block the request
        if not self.vault.docapi_url:
            raise Exception('docapi is not enabled for this vv environment')

    def get_file_stream(self, file_id):
        """
        get file stream of file by file_id
        :param file_id: string uuid4
        :return: dict
        """
        endpoint = FILES_URL + '/' + REVISIONS_URL + '/' + file_id
        request_url = self.vault.docapi_url + '/api/v1/' + endpoint
        headers = self.vault.get_jwt_auth_headers()
        resp = requests.get(request_url, headers=headers, stream=True)

        return resp
