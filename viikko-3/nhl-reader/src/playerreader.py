import requests

class PlayerReader:
    def __init__(self, url, req = requests):
        self.url = url
        self.requests = req

    def fetch (self):
        return requests.get(self.url).json()