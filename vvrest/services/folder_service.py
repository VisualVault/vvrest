import requests
from ..constants import FOLDERS_URL, DOCUMENTS_URL, INDEX_FIELDS_URL, SELECT_OPTIONS_URL, WORKFLOW_ASSIGNMENTS_URL


class FolderService:
    def __init__(self, vault):
        """
        :param vault: Vault
        """
        self.vault = vault

    def get_folder_search(self, folder_path):
        """
        search for a folder by folderPath
        :param folder_path: string
        :return: dict
        """
        endpoint = FOLDERS_URL + '?folderPath=' + folder_path
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_folder(self, folder_id):
        """
        get a folder by id
        :param folder_id: string uuid4
        :return: dict
        """
        endpoint = FOLDERS_URL + '/' + folder_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_sub_folders(self, folder_id):
        """
        get all sub folders of a folder by id
        :param folder_id: string uuid4
        :return: dict
        """
        endpoint = FOLDERS_URL + '/' + folder_id + '/' + FOLDERS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_folder_documents(self, folder_id):
        """
        get all documents of a folder by id
        :param folder_id: string uuid4
        :return: dict
        """
        endpoint = FOLDERS_URL + '/' + folder_id + '/' + DOCUMENTS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_folder_index_fields(self, folder_id):
        """
        get all index fields of a folder by id
        :param folder_id: string uuid4
        :return: dict
        """
        endpoint = FOLDERS_URL + '/' + folder_id + '/' + INDEX_FIELDS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_folder_index_field(self, folder_id, field_id):
        """
        get a folder index field
        :param folder_id: string uuid4
        :param field_id: string uuid4
        :return: dict
        """
        endpoint = FOLDERS_URL + '/' + folder_id + '/' + INDEX_FIELDS_URL + '/' + field_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def get_folder_index_field_select_options(self, folder_id, field_id):
        """
        get select options for a folder index field
        TODO: unittest
        :param folder_id: string uuid4
        :param field_id: string uuid4
        :return: dict
        """
        endpoint = FOLDERS_URL + '/' + folder_id + '/' + INDEX_FIELDS_URL + '/' + field_id + '/' + SELECT_OPTIONS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def new_folder(self, name, description, allow_revisions):
        """
        creates a new folder
        :param name: string
        :param description: string
        :param allow_revisions: bool
        :return: dict
        """
        request_url = self.vault.base_url + FOLDERS_URL
        headers = self.vault.get_auth_headers()

        payload = {
            'name': name,
            'description': description,
            'allowRevisions': allow_revisions
        }

        resp = requests.post(request_url, data=payload, headers=headers).json()

        return resp

    def new_sub_folder(self, folder_id, name, description, allow_revisions):
        """
        creates a new sub folder
        :param folder_id: string uuid4
        :param name: string
        :param description: string
        :param allow_revisions: bool
        :return: dict
        """
        request_url = self.vault.base_url + FOLDERS_URL + '/' + folder_id
        headers = self.vault.get_auth_headers()

        payload = {
            'name': name,
            'description': description,
            'allowRevisions': allow_revisions
        }

        resp = requests.post(request_url, data=payload, headers=headers).json()

        return resp

    def update_folder_index_field(self, folder_id, field_id, required, default_value, query_display_field='',
                                  query_value_field='', query_id='00000000-0000-0000-0000-000000000000',
                                  drop_down_list_id='00000000-0000-0000-0000-000000000000'):
        """
        update a folder index field
        :param folder_id: string uuid4
        :param field_id: string uuid4
        :param required: bool
        :param default_value: string
        :param query_display_field: string
        :param query_value_field: string
        :param query_id: string uuid4
        :param drop_down_list_id: string uuid4
        :return: dict
        """
        endpoint = 'folders/' + folder_id + '/indexfields/' + field_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()

        payload = {
            'dropDownListId': drop_down_list_id,
            'queryId': query_id,
            'queryValueField': query_value_field,
            'queryDisplayField': query_display_field,
            'required': required,
            'defaultValue': default_value
        }

        resp = requests.put(request_url, data=payload, headers=headers).json()

        return resp

    def reassign_workflow_relations(self, folder_id, wf_id, event_type, apply_to_children, include_this_folder):
        """
        re assign workflow relations for a folder
        TODO: event_type documentation and unittest
        :param folder_id: string uuid4
        :param wf_id: string uuid4
        :param event_type: int
        :param apply_to_children: bool
        :param include_this_folder: bool
        :return: dict
        """
        endpoint = 'folders/' + folder_id + '/' + WORKFLOW_ASSIGNMENTS_URL
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()

        payload = {
            'wfId': wf_id,
            'eventType': event_type,
            'applyToChildren': apply_to_children,
            'includeThisFolder': include_this_folder
        }

        resp = requests.put(request_url, data=payload, headers=headers).json()

        return resp
