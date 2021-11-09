from time import sleep

import requests


class ClienteHttp():

    def __init__(self,url,retry=0 , retry_codes=[]):
        self.url=url
        self.retry= retry
        self.retry_codes=retry_codes

    def get(self,  payload = {}, headers = {}) -> dict:
      for i in range(self.retry +1):
        response = requests.request("GET", self.url, headers=headers,
                                  data=payload)
        print(f'{i},{response.status_code}')
        if response.status_code == 200 \
                or response.status_code not in self.retry_codes:
            return response.json()
        sleep(0.00001 * (10**i))


if __name__ == '__main__':
    cliente=ClienteHttp('http://localhost:2121/demo/',50,[500,503,301])
    cliente.get()

