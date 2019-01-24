import unittest
from .setup import setup_test_suite
from .utilities import get_vault_object
from .auth_service_test import AuthServiceTest
from .document_service_test import DocumentServiceTest
from .email_service_test import EmailServiceTest
from .file_service_test import FileServiceTest
from .folder_service_test import FolderServiceTest
from .form_service_test import FormServiceTest
from .group_service_test import GroupServiceTest
from .index_field_service_test import IndexFieldServiceTest
from .site_service_test import SiteServiceTest
from .user_service_test import UserServiceTest

setup_test_suite()  # setup VVRestTestSuite

vault = get_vault_object()
AuthServiceTest.vault = vault
DocumentServiceTest.vault = vault
EmailServiceTest.vault = vault
FileServiceTest.vault = vault
FolderServiceTest.vault = vault
FormServiceTest.vault = vault
GroupServiceTest.vault = vault
IndexFieldServiceTest.vault = vault
SiteServiceTest.vault = vault
UserServiceTest.vault = vault


if __name__ == '__main__':
    unittest.main()
