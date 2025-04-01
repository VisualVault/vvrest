import requests

from ..constants import SEARCH_URL

class DocApiSearchService:
    def __init__(self, vault):
        """
        :param vault: Vault
        """
        self.vault = vault
        
        # if docapi is not enabled block the request
        if not self.vault.docapi_url:
            raise Exception('docapi is not enabled for this vv environment')

    def get_documents_by_folder(self, folder_id, archive_type=None, sort_by=None, sort_direction=None,
                                role_security=False, take=10, page=0, q=None):
        """
        search documents by folder from the doc api
        :param folder_id: string (UUID)
        :param archive_type: int (0, 1, 2, 3)
        :param sort_by: string
        :param sort_direction: string
        :param role_security: boolean
        :param take: int (default 10)
        :param page: int (default 0)
        :param q: string (query string)
        :return: dict (API response)
        """
        endpoint = f'{SEARCH_URL}/folder/{folder_id}'
        request_url = f'{self.vault.docapi_url}/api/v1/{endpoint}'
        headers = self.vault.get_jwt_auth_headers()
        
        params = {
            "archiveType": archive_type,
            "sortBy": sort_by,
            "sortDirection": sort_direction,
            "roleSecurity": str(role_security).lower(),
            "take": take,
            "page": page,
            "q": q
        }

        # remove None values from params
        params = {k: v for k, v in params.items() if v is not None}
        
        resp = requests.get(request_url, headers=headers, params=params)
        return resp.json()
