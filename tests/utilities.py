import json
from uuid import uuid4
from vvrest.vault import Vault
from .settings import credentials_file, parameters_file


def get_vault_object():
    """
    :return: Vault
    """
    with open(credentials_file) as credentials_json:
        credentials = json.load(credentials_json)

    vault = Vault(credentials['url'], credentials['customer_alias'], credentials['database_alias'],
                  credentials['client_id'], credentials['client_secret'])

    return vault


def generate_random_uuid():
    """
    :return: string uuid4
    """
    uuid = str(uuid4())

    return uuid


def get_parameters_json():
    """
    :return: dict
    """
    with open(parameters_file) as parameters_json:
        parameters = json.load(parameters_json)

    return parameters


def get_test_email_address():
    """
    :return: string
    """
    with open(credentials_file) as credentials_json:
        credentials = json.load(credentials_json)

    return credentials['email_address']
