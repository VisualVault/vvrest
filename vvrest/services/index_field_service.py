import requests
from ..constants import INDEX_FIELDS_URL, FOLDERS_URL


class IndexFieldService:
    def __init__(self, vault):
        self.vault = vault

    def get_index_fields(self, query=''):
        """
        get all index fields or filter by query
        :param query: string, example: "label = 'TestField'"
        :return: dict
        """
        request_url = self.vault.base_url + INDEX_FIELDS_URL
        if query:
            request_url += '?q=' + query

        headers = self.vault.get_auth_headers()
        resp = requests.get(request_url, headers=headers).json()

        return resp

    def create_index_field(self, label, description, field_type, required, default_value, query_value_field='',
                           query_display_field='', query_id='00000000-0000-0000-0000-000000000000',
                           drop_down_list_id='00000000-0000-0000-0000-000000000000'):
        """
        creates a new index field definition
        :param label: string
        :param description: string
        :param field_type: int example: TODO: document field_type ENUM
        :param required: bool
        :param default_value: string
        :param query_value_field: string, default: empty string
        :param query_display_field: string, default: empty string
        :param query_id: string uuid4, default: empty uuid4
        :param drop_down_list_id: string uuid4, default: empty uuid4
        :return: dict
        """
        request_url = self.vault.base_url + INDEX_FIELDS_URL
        headers = self.vault.get_auth_headers()

        payload = {
            'label': label,
            'description': description,
            'fieldType': field_type,
            'queryId': query_id,
            'dropDownListId': drop_down_list_id,
            'queryValueField': query_value_field,
            'queryDisplayField': query_display_field,
            'required': required,
            'defaultValue': default_value
        }

        resp = requests.post(request_url, headers=headers, data=payload).json()

        return resp

    def update_index_field(self, index_field_id, label, description, required, default_value, query_value_field='',
                           query_display_field='', query_id='00000000-0000-0000-0000-000000000000',
                           drop_down_list_id='00000000-0000-0000-0000-000000000000'):
        """
        updates an index field definition
        :param index_field_id: string uuid4
        :param label: string
        :param description: string
        :param required: bool
        :param default_value: string
        :param query_value_field: string, default: empty string
        :param query_display_field: string, default: empty string
        :param query_id: string uuid4, default: empty uuid4
        :param drop_down_list_id: string uuid4, default: empty uuid4
        :return: dict
        """
        request_url = self.vault.base_url + INDEX_FIELDS_URL + '/' + index_field_id
        headers = self.vault.get_auth_headers()

        payload = {
            'label': label,
            'description': description,
            'queryId': query_id,
            'dropDownListId': drop_down_list_id,
            'queryValueField': query_value_field,
            'queryDisplayField': query_display_field,
            'required': required,
            'defaultValue': default_value
        }

        resp = requests.put(request_url, headers=headers, data=payload).json()

        return resp

    def relate_index_field_to_folder(self, field_id, folder_id):
        endpoint = INDEX_FIELDS_URL + '/' + field_id + '/' + FOLDERS_URL + '/' + folder_id
        request_url = self.vault.base_url + endpoint
        headers = self.vault.get_auth_headers()
        resp = requests.put(request_url, headers=headers).json()

        return resp
