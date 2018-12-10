import unittest
import os
from .utilities import get_vault_object, generate_random_uuid
from vvrest.services.file_service import FileService


class FileTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vault = get_vault_object()
        cls.document_id = '810013e6-50fa-e811-a9cf-8b72d90dd505'
        cls.document_revision_id = '8fefa9b6-56fa-e811-a995-a3d452a1c2f6'
        cls.file_path = os.getcwd() + '/tests/docs'
        cls.file_name = 'test_docs.txt'
        cls.file_upload_name = 'test_file.txt'

    def test_file_download(self):
        """
        tests FileService.file_download
        """
        files = os.listdir(self.file_path)  # validate file does not exist
        self.assertNotIn(self.file_name, files)

        file_service = FileService(self.vault)
        file_service.file_download(self.document_revision_id, self.file_path + '/' + self.file_name)  # download file

        files = os.listdir(self.file_path)  # validate file exists
        self.assertIn(self.file_name, files)

        os.remove(self.file_path + '/' + self.file_name)  # delete file
        files = os.listdir(self.file_path)
        self.assertNotIn(self.file_name, files)  # validate file is deleted

    def test_file_download_by_search(self):
        """
        tests FileService.file_download_by_search
        """
        files = os.listdir(self.file_path)  # validate file does not exist
        self.assertNotIn(self.file_name, files)

        file_service = FileService(self.vault)
        file_service.file_download_by_search("id='" + self.document_revision_id + "'",
                                             self.file_path + '/' + self.file_name)  # download file

        files = os.listdir(self.file_path)  # validate file exists
        self.assertIn(self.file_name, files)

        os.remove(self.file_path + '/' + self.file_name)  # delete file
        files = os.listdir(self.file_path)
        self.assertNotIn(self.file_name, files)  # validate file is deleted

    def test_file_upload(self):
        """
        test FileService.file_upload
        """
        expected_revision = generate_random_uuid()
        file_service = FileService(self.vault)
        resp = file_service.file_upload(self.document_id, 'unittest', expected_revision, 'unittest change reason',
                                        'Released', '', 'unittest.txt', self.file_path + '/' + self.file_upload_name)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)
        self.assertEqual(resp['data']['revision'], expected_revision)
