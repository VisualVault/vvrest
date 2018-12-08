import unittest
from .authentication import AuthenticationTest
from .documents import DocumentTest
from .emails import EmailTest
from .files import FileTest


class RestClientTestSuite(unittest.TestCase):
    AuthenticationTest()
    DocumentTest()
    EmailTest()
    FileTest()


if __name__ == '__main__':
    unittest.main()
