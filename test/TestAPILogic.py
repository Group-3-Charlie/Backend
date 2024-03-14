import unittest
from unittest.mock import MagicMock, patch
from flask import Flask

from code.api_logic import APILogic
class TestAPILogic(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_upload_no_file_part(self):
        with self.app.test_request_context('/upload', method='POST'):
            response = APILogic.upload(self.app.test_request_context().request)
            self.assertEqual(response[1], 400)
            self.assertIn(b'No file part in the request', response[0].data)

    def test_upload_no_file_selected(self):
        with self.app.test_request_context('/upload', method='POST',
                                           data={'file': MagicMock(filename='')}):
            response = APILogic.upload(self.app.test_request_context())
            self.assertEqual(response[1], 400)
            self.assertIn(b'No file selected for uploading', response[0].data)

    def test_upload_invalid_file_extension(self):
        with self.app.test_request_context('/upload', method='POST',
                                           data={'file': MagicMock(filename='test.txt')}):
            response = APILogic.upload(self.app.test_request_context())
            self.assertEqual(response[1], 400)
            self.assertIn(b'Only CSV files are allowed', response[0].data)

    # Add more test methods for other functionalities like select_target and predict

if __name__ == '__main__':
    unittest.main()
