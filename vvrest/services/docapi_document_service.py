import requests

from ..constants import DOCUMENTS_URL, REVISIONS_URL


class DocApiDocumentService:
    def __init__(self, vault):
        """
        :param vault: Vault
        """
        self.vault = vault
        
        # if docapi is not enabled block the request
        if not self.vault.docapi_url:
            raise Exception('docapi is not enabled for this vv environment')

    def get_document_revision(self, revision_id):
        """
        get a specific revision of a document by revisionId
        :param revision_id: string uuid4
        :return: dict
        """
        endpoint = DOCUMENTS_URL + '/' + REVISIONS_URL + '/' + revision_id
        request_url = self.vault.docapi_url + '/api/v1/' + endpoint
        headers = self.vault.get_jwt_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp
