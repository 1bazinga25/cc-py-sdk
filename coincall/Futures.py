from .client import Client

class FuturesAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', diff='3000', use_server_time=False, domain = 'https://api.coincall.com',debug = True):
        Client.__init__(self, api_key, api_secret_key, diff, use_server_time, domain, debug)

    def get_symbols(self):
        """
        |
        | **Get Symbol Information**
        | *Get futures symbol information.*

        :API endpoint: ``GET /open/futures/market/symbol/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-symbol-information-signed
        |
        """

        params = {}
        url_path = "/open/futures/market/symbol/v1"
        return self._request("GET", url_path, params)
    
    def get_orderbook(self, symbol):
        """
        |
        | **Get OrderBook**
        | *Get futures orderbook for 100 depth.*

        :API endpoint: ``GET /open/futures/order/orderbook/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-symbol-information-signed
        |
        """

        params = {
            "symbol": symbol
        }
        url_path = "/open/futures/order/orderbook/v1"
        return self._request("GET", url_path, params)

        