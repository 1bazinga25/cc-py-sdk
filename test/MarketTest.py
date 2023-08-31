import unittest
from coincall import Public

class publickTest(unittest.TestCase):
    def setUp(self):
        api_key = '-1'
        api_secret_key = '-1'
        self.publicApi = Public.PublicAPI(api_key, api_secret_key, use_server_time=False)


    def test_get_server_time(self):
        print(self.publicApi.get_server_time())

if __name__ == '__main__':
    unittest.main()