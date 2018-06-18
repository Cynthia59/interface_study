import requests
import json

class RunMain():

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        elif method == 'POST':
            res = self.send_post(url, data)
        return res

if __name__ == '__main__':

    print('test')