from .context import whmapi
import unittest


class HeaderContrsuctionTest(unittest.TestCase):
    def setUp(self):
        self.header = 'sampleaccesshash'
        self.default_user = 'root'
        self.api_client = whmapi.APIClient(
            api_acc_hash=self.header)

    def header_lenght_test(self):
        headers = self.api_client._auth_headers()
        self.assertGreaterEqual(len(headers), 1)

    def header_structure_test(self):
        headers = self.api_client._auth_headers()
        for header in headers:
            if header[0] == 'Authorization':
                self.assertNotIn('\n', header[1])
                self.assertIn(self.header, header[1])
