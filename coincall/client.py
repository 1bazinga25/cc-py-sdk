import json

import httpx

from . import utils, exceptions


class Client(object):

    def __init__(self, api_key='-1', api_secret_key='-1', diff='3000', use_server_time=False, base_api="https://api.coincall.com", debug='True'):
        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.diff = diff
        self.use_server_time = use_server_time
        self.domain = base_api
        self.debug = debug
        self.client = httpx.Client(base_url=base_api, http2=True)

    def _request(self, method, request_path, params):
        if method == "GET":
            request_path = request_path + utils.parse_params_to_str(params)
        timestamp = utils.get_timestamp()
        if self.use_server_time:
            timestamp = self._get_timestamp()
        body = json.dumps(params) if method == "POST" else ""
        if self.API_KEY != '-1':
            sign = utils.sign(utils.pre_hash(timestamp, method, request_path, str(
                body), self.API_KEY, self.diff, self.debug), self.API_SECRET_KEY, self.debug)
            header = utils.get_header(
                self.API_KEY, sign, timestamp, self.diff, self.debug)
        else:
            header = utils.get_header_no_sign(self.debug)
        response = None
        if self.debug == True:
            print('domain:', self.domain)
            print('url:', request_path)
        if method == "GET":
            response = self.client.get(request_path, headers=header)
        elif method == "POST":
            response = self.client.post(
                request_path, data=body, headers=header)
        if response.status_code != httpx.codes.OK:
            print(response.text)
        return response.json()

    def _request_without_params(self, method, request_path):
        return self._request(method, request_path, {})

    def _request_with_params(self, method, request_path, params):
        return self._request(method, request_path, params)

    def _get_timestamp(self):
        request_path = self.domain + "/time"
        response = self.client.get(request_path)
        if response.status_code == 200:
            return response.json()['data']['serverTime']
        else:
            return ""
