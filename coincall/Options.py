from .client import Client

class OptionsAPI(Client):

    def __init__(self, api_key='-1', api_secret_key='-1', diff='3000', use_server_time=False, domain = 'https://api.coincall.com',debug = True):
        Client.__init__(self, api_key, api_secret_key, diff, use_server_time, domain, debug)

    def get_instruments(self, base):
        """
        |
        | **Get Instruments**
        | *Get all options instruments.*

        :API endpoint: ``GET /open/option/getInstruments/{}``
        :API doc: https://docs.coincall.com/#futures-endpoint-get-symbol-information-signed
        :Parameter: query string
        |
        """

        params = {}
        url_path = "/open/option/getInstruments/{}".format(base)
        return self._request("GET", url_path, params)