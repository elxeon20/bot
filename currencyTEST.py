import time

import requests


class Currency:
    def __init__(self):
        pass

    @staticmethod
    def get_info(asset, tradeType, payTypes):
        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Length": "123",
            "content-type": "application/json",
            "Host": "p2p.binance.com",
            "Origin": "https://p2p.binance.com",
            "Pragma": "no-cache",
            "TE": "Trailers",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
        }
        data = {
            "asset": asset,
            "fiat": "UAH",
            "merchantCheck": False,
            "page": 1,
            "payTypes": payTypes,
            "publisherType": None,
            "rows": 10,
            "tradeType": tradeType
        }

        r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
        r = r.text.replace('null', '0').replace('true', 'True').replace('false', 'False')
        r = eval(r)
        # print(r)
        data = []
        for i in range(10):
            price = round(float(r.get('data')[i].get('adv').get('price')), 2)
            amount = round(float(r.get('data')[i].get('adv').get('surplusAmount')), 2)
            min = round(float(r.get('data')[i].get('adv').get('minSingleTransAmount')), 2)

            data.append((f"Цена {price} | кол-во {amount} грн. | мин обьем {min} грн"))
        return data

    def restart(self):
        while True:
            time.sleep(3)
            print(self.get_info("UAH", "SELL", ['PrivatBank']))
            print(self.get_info("UAH", "BUY", ['PrivatBank']))

Currency().restart()

# Currency.get_info("UAH", "SELL",['PrivatBank'])
