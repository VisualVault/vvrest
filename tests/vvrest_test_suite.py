import unittest
from .auth_service_test import AuthServiceTest
from .document_service_test import DocumentServiceTest
from .email_service_test import EmailServiceTest
from .file_service_test import FileServiceTest
from .folder_service_test import FolderServiceTest
from .group_service_test import GroupServiceTest
from .index_field_service_test import IndexFieldServiceTest
from .site_service_test import SiteServiceTest
from .user_service_test import UserServiceTest


class VVRestTestSuite(unittest.TestCase):
    AuthServiceTest()
    DocumentServiceTest()
    EmailServiceTest()
    FileServiceTest()
    FolderServiceTest()
    GroupServiceTest()
    IndexFieldServiceTest()
    SiteServiceTest()
    UserServiceTest()


if __name__ == '__main__':
    unittest.main()
