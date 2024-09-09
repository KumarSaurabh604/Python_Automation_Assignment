import requests
from trello_api_framework.utils.config_parser import ConfigParser


class TrelloApiClient:
    def __init__(self):
        config = ConfigParser().get_trello_config()
        self.api_key = config['api_key']
        self.token = config['token']
        self.base_url = config['base_url']
        self.card_id = config['card_id']
        self.invalid_card_id = config['invalid_card_id']
        self.id_list = config['id_list']
        self.invalid_id_list = config['invalid_id_list']

    def _get_headers(self):
        return {
            'Accept': 'application/json'
        }

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        params = {
            "key": self.api_key,
            "token": self.token
        }
        headers = self._get_headers()
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self, endpoint, param=None):
        url = f"{self.base_url}/{endpoint}"
        params = {
            'key': self.api_key,
            'token': self.token
        }
        params.update(param)
        headers = self._get_headers()
        response = requests.post(url, params=params, headers=headers)
        return response

    def put(self, endpoint, param=None):
        url = f"{self.base_url}/{endpoint}"
        params = {
            'key': self.api_key,
            'token': self.token
        }
        params.update(param)
        headers = self._get_headers()
        response = requests.put(url, params=params, headers=headers)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        params = {
            'key': self.api_key,
            'token': self.token
        }
        headers = self._get_headers()
        response = requests.delete(url, params=params, headers=headers)
        return response
