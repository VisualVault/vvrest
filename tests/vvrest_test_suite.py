import unittest
from .auth_service_test import AuthServiceTest
from .document_service_test import DocumentServiceTest
from .email_service_test import EmailServiceTest
from .file_service_test import FileServiceTest
from .folder_service_test import FolderServiceTest
from .group_service_test import GroupServiceTest


class VVRestTestSuite(unittest.TestCase):
    AuthServiceTest()
    DocumentServiceTest()
    EmailServiceTest()
    FileServiceTest()
    FolderServiceTest()
    GroupServiceTest()


if __name__ == '__main__':
    unittest.main()
