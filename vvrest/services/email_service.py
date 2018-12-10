import requests
from ..constants import EMAILS_URL


class EmailService:
    def __init__(self, vault):
        """
        :param vault: Vault
        """
        self.vault = vault

    def send_email(self, recipient, cc_recipient, subject, body, has_attachments, documents):
        """
        :param recipient: string, example: test@test.com
        :param cc_recipient: string, example: test@test.com,test2@aol.com
        :param subject: string
        :param body: string
        :param has_attachments: bool
        :param documents: list(string uuid4)
        :return: dict
        """
        request_url = self.vault.base_url + EMAILS_URL
        headers = self.vault.get_auth_headers()

        payload = {
            'recipients': recipient,
            'ccrecipients': cc_recipient,
            'subject': subject,
            'body': body,
            'hasAttachments': has_attachments,
            'documents': documents
        }

        resp = requests.post(request_url, data=payload, headers=headers).json()

        return resp
