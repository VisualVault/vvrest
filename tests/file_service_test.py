import unittest
import os
from .utilities import get_vault_object, generate_random_uuid
from vvrest.services.file_service import FileService


class FileServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()
        cls.document_id = '810013e6-50fa-e811-a9cf-8b72d90dd505'
        cls.document_revision_id = '8fefa9b6-56fa-e811-a995-a3d452a1c2f6'
        cls.file_path = os.getcwd() + '/tests/docs'
        cls.file_upload_name = 'test_file.txt'

    def test_get_file_stream(self):
        """
        tests FileService.get_file_stream
        """
        file_service = FileService(self.vault)
        stream = file_service.get_file_stream(self.document_revision_id)
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')

    def test_file_upload(self):
        """
        test FileService.file_upload and FileService.get_file_stream_by_search
        """
        expected_revision = generate_random_uuid()
        file_service = FileService(self.vault)
        resp = file_service.file_upload(self.document_id, 'unittest', expected_revision, 'unittest change reason',
                                        'Released', '', 'unittest.txt', self.file_path + '/' + self.file_upload_name)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)
        self.assertEqual(resp['data']['revision'], expected_revision)

        new_file_id = resp['data']['id']
        stream = file_service.get_file_stream_by_search("[id]='" + new_file_id + "'")
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')
