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

        :API endpoint: ``GET /open/futures/order/orderbook/v1/{}``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-symbol-information-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/futures/order/orderbook/v1/{}".format(symbol)
        return self._request("GET", url_path, params)
    
    def get_lasttrade(self, symbol):
        """
        |
        | **Get Last Trade**
        | *Get futures last trade.*

        :API endpoint: ``GET /open/futures/trade/lasttrade/v1/{}``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-last-trade-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/futures/trade/lasttrade/v1/{}".format(symbol)
        return self._request("GET", url_path, params)
    
    def get_leverage(self, symbol):
        """
        |
        | **Get leverage**
        | *Get current futrues leverage.*

        :API endpoint: ``GET /open/futures/leverage/current/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-leverage-signed
        :Parameter: query string
        |
        """

        params = {
            "symbol": symbol
        }
        url_path = "/open/futures/leverage/current/v1"
        return self._request("GET", url_path, params)
    
    def set_leverage(self, symbol, leverage):
        """
        |
        | **Set Leverage**
        | *Set futures leverage.*

        :API endpoint: ``POST /open/futures/leverage/set/v1``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-leverage-signed
        :Parameter: request body
        |
        """

        params = {
            "symbol": symbol,
            "leverage": leverage
        }
        url_path = "/open/futures/leverage/set/v1"
        return self._request("POST", url_path, params)

        