import unittest
from .utilities import get_vault_object, generate_random_uuid, get_parameters_json
from vvrest.services.file_service import FileService
from .settings import test_file_path


class FileServiceTest(unittest.TestCase):
    vault = None

    @classmethod
    def setUpClass(cls):
        if not cls.vault:
            cls.vault = get_vault_object()

        test_parameters = get_parameters_json()
        cls.document_id = test_parameters['document_id']
        cls.document_revision_id = test_parameters['document_revision_id']
        cls.file_path = test_file_path
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
        stream = file_service.get_file_stream(new_file_id)
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')

        # TODO: functionality change in vv 5.0?
        # stream = file_service.get_file_stream_by_search("[id]='" + new_file_id + "'")
        # stream_stats = vars(stream)
        # self.assertEqual(stream_stats['status_code'], 200)
        # self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')

    def test_file_upload_check_in(self):
        """
        validate FileService.file_upload check_in functionality
        """
        # validate default checkIn
        expected_revision = generate_random_uuid()
        file_service = FileService(self.vault)
        resp = file_service.file_upload(self.document_id, 'unittest', expected_revision, 'unittest change reason',
                                        'Released', '', 'unittest.txt', self.file_path + '/' + self.file_upload_name)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)
        self.assertEqual(resp['data']['revision'], expected_revision)
        self.assertEqual(resp['data']['checkInStatus'], 0)

        new_file_id = resp['data']['id']
        stream = file_service.get_file_stream(new_file_id)
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')

        # validate checkIn True
        expected_revision = generate_random_uuid()
        file_service = FileService(self.vault)
        resp = file_service.file_upload(self.document_id, 'unittest', expected_revision, 'unittest change reason',
                                        'Released', '', 'unittest.txt', self.file_path + '/' + self.file_upload_name,
                                        check_in=0)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)
        self.assertEqual(resp['data']['revision'], expected_revision)
        self.assertEqual(resp['data']['checkInStatus'], 0)

        new_file_id = resp['data']['id']
        stream = file_service.get_file_stream(new_file_id)
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')

        # validate checkIn False
        expected_revision = generate_random_uuid()
        file_service = FileService(self.vault)
        resp = file_service.file_upload(self.document_id, 'unittest', expected_revision, 'unittest change reason',
                                        'Released', '', 'unittest.txt', self.file_path + '/' + self.file_upload_name,
                                        check_in=1)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)
        self.assertEqual(resp['data']['revision'], expected_revision)
        self.assertEqual(resp['data']['checkInStatus'], 1)

        new_file_id = resp['data']['id']
        stream = file_service.get_file_stream(new_file_id)
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')
