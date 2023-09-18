import unittest
from coincall import Futures

class futuresTest(unittest.TestCase):
    def setUp(self):
        api_key = '-1'
        api_secret_key = '-1'
        self.futuresApi = Futures.FuturesAPI(api_key, api_secret_key, use_server_time=False)


    def test_get_symbols(self):
        print(self.futuresApi.get_symbols())

    def test_get_depth(self):
        print(self.futuresApi.get_depth(symbol='BTCUSD'))

if __name__ == '__main__':
    unittest.main()