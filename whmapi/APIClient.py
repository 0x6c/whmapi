try:
    from urlparse import urljoin
    from urllib2 import build_opener
except ImportError:
    from urllib.parse import urljoin
    from urllib.request import build_opener
import json
class APIClient(object):
    """WHM API client class"""
    def __init__(self,
                 host_uri='https://127.0.0.1:2087',
                 api_user='root',
                 api_type='json-api',
                 api_version=1,
                 api_acc_hash=None):
        super(APIClient, self).__init__()
        self.host_uri = host_uri
        self.api_user = api_user
        self.api_type = api_type
        self.api_version = api_version
        self.api_acc_hash = api_acc_hash or self.__read_accesshash()
        self.opener = self._get_opener()

    def __read_accesshash(self, acc_hash_path='/root/.accesshash'):
        """
        Read accesshash file from root directory(if not specified another).
        """
        with open(acc_hash_path) as f:
            access_hash = f.read()
            hash_string = ''.join(
                [hl.rstrip('\n') for hl in access_hash.splitlines()]
            )
            return hash_string

    def get_url_for(self, function, req_params={}):
        """ URL constructor for API calls.
        @function: function name to vbe called from WHMApi list.
        @params: request params.
        """
        params = '&'.join(['{pn}={pv}'.format(pn=pn, pv=pv)
                           for (pn, pv) in req_params.items()])
        url_path = '{at}/{fc}?api.version={av}&{pm}'.format(
            at=self.api_type,
            fc=function,
            av=self.api_version,
            pm=params)
        constrcuted = urljoin(self.host_uri, url_path)
        # Dirty hack to prevent few if's
        # This allows us to ignore case when paramse were empty.
        return constrcuted.rstrip('&')

    def _auth_headers(self):
        headers = [
            ('Authorization', 'WHM {us}:{ah}'.format(
                us=self.api_user,
                ah=self.api_acc_hash))
        ]
        return headers

    def _get_opener(self):
        """Retrieve URLOpenerDirector object with required headers"""
        opener = build_opener()
        opener.addheaders = self._auth_headers()
        return opener

    def call(self, function, req_params={}):
        """ Generate API call with specified params for specified function """
        uri = self.get_url_for(function, req_params)
        result = self.opener.open(uri)
        return json.loads(result.read().decode('utf-8'))
