import json
from uuid import uuid4
from random import choice

from vvrest.vault import Vault

from .settings import credentials_file, parameters_file


def get_vault_object(user_web_token=None, jwt=None, docapi_enabled=True):
    """
    :param user_web_token: string UUID(version=4), used for user impersonation
    :param jwt: str, JSON Web Token
    :param auto_jwt: bool
    :return: Vault
    """
    with open(credentials_file) as credentials_json:
        credentials = json.load(credentials_json)
    
    audience = None
    if 'audience' in credentials:
        if credentials['audience'] not in ["", "null"]:
            audience = credentials['audience']

    if docapi_enabled:
        vault = Vault(credentials['url'], credentials['customer_alias'], credentials['database_alias'],
                      credentials['client_id'], credentials['client_secret'], user_web_token, jwt, audience)
    else:
        vault = Vault(credentials['docapi_not_enabled']['url'], credentials['docapi_not_enabled']['customer_alias'], credentials['docapi_not_enabled']['database_alias'],
                      credentials['docapi_not_enabled']['client_id'], credentials['docapi_not_enabled']['client_secret'], user_web_token, jwt, audience)

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


def get_random_string(length):
    """
    :param length: int
    :return: string
    """
    char_choices = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'  # TODO: use random.choices with python upgrade
    random_string = ''.join(choice(char_choices) for i in range(length))

    return random_string
