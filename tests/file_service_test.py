import unittest

from io import BytesIO
from vvrest.services.file_service import FileService

from .utilities import get_vault_object, generate_random_uuid, get_parameters_json
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
                                        check_in=True)

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
                                        check_in=False)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)
        self.assertEqual(resp['data']['revision'], expected_revision)
        self.assertEqual(resp['data']['checkInStatus'], 1)

        new_file_id = resp['data']['id']
        stream = file_service.get_file_stream(new_file_id)
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')

    def test_file_stream_upload(self):
        """
        test FileService.file_stream_upload
        """
        file_service = FileService(self.vault)

        # test sending a file stream through with open
        expected_revision = generate_random_uuid()
        with open(self.file_path + '/' + self.file_upload_name, 'rb') as file_stream:
            resp = file_service.file_stream_upload(self.document_id, 'unittest', expected_revision, 'unittest change reason',
                                                   'Released', '', 'unittest.txt', file_stream, True)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)
        self.assertEqual(resp['data']['revision'], expected_revision)

        new_file_id = resp['data']['id']
        stream = file_service.get_file_stream(new_file_id)
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')

        # test sending an in memory file stream (BytesIO) written from open
        expected_revision = generate_random_uuid()
        with open(self.file_path + '/' + self.file_upload_name, 'rb') as file_stream:
            with BytesIO() as memory_stream:
                memory_stream.writelines(file_stream)
                resp = file_service.file_stream_upload(self.document_id, 'unittest', expected_revision, 'unittest change reason',
                                                       'Released', '', 'unittest.txt', memory_stream.getvalue(), True)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)
        self.assertEqual(resp['data']['revision'], expected_revision)

        new_file_id = resp['data']['id']
        stream = file_service.get_file_stream(new_file_id)
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')

        # test sending an in memory file stream (BytesIO) written from stream url
        expected_revision = generate_random_uuid()
        with file_service.get_file_stream(new_file_id) as file_stream:
            stream_stats = vars(file_stream)
            self.assertEqual(stream_stats['status_code'], 200)
            self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')
            with BytesIO(file_stream.content) as memory_stream:
                resp = file_service.file_stream_upload(self.document_id, 'unittest', expected_revision, 'unittest change reason',
                                                       'Released', '', 'unittest.txt', memory_stream.getvalue(), True)

        self.assertEqual(resp['meta']['status'], 200)
        self.assertEqual(resp['data']['documentId'], self.document_id)
        self.assertEqual(resp['data']['revision'], expected_revision)

        new_file_id = resp['data']['id']
        stream = file_service.get_file_stream(new_file_id)
        stream_stats = vars(stream)
        self.assertEqual(stream_stats['status_code'], 200)
        self.assertEqual(stream_stats['headers']['Content-Type'], 'application/octet-stream')
