from .context import whmapi
import unittest


class UrlRendererTest(unittest.TestCase):
    def setUp(self):
        self.api_client = whmapi.APIClient(api_acc_hash="sampleaccesshash")

    def without_params_test(self):
        url = self.api_client.get_url_for(
            function='listaccts')
        self.assertEqual(
            'https://127.0.0.1:2087/json-api/listaccts?api.version=1',
            url
        )

    def with_params_test(self):
        params = {
            'searchtype': 'user',
            'search': 'example'
        }
        url = self.api_client.get_url_for(
            function='listaccts',
            req_params=params
        )

        self.assertEqual(
            'https://127.0.0.1:2087/json-api/listaccts?api.version=1&search=example&searchtype=user',
            url)

    def with_empty_function_test(self):
        with self.assertRaises(TypeError):
            self.api_client.get_url_for()
