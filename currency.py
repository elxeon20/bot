import requests


class Currency:
    def __init__(self, asset, tradeType, payTypes):
        self.asset = asset
        self.tradeType = tradeType
        self.payTypes = payTypes

    def get_info(self):
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
            "asset": self.asset,
            "fiat": "UAH",
            "merchantCheck": False,
            "page": 1,
            "payTypes": self.payTypes,
            "publisherType": None,
            "rows": 10,
            "tradeType": self.tradeType
        }

        r = requests.post('https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search', headers=headers, json=data)
        r = r.text.replace('null', '0').replace('true', 'True').replace('false', 'False')
        r = eval(r)
        # print(r)
        return r

    def data_convert(self):
        data = []
        r = Currency.get_info(self)
        for i in range(10):
            price = round(float(r.get('data')[i].get('adv').get('price')), 2)
            amount = round(float(r.get('data')[i].get('adv').get('surplusAmount')), 2)
            min = round(float(r.get('data')[i].get('adv').get('minSingleTransAmount')), 2)

            data.append((f"Цена {price} | кол-во {amount} грн. | мин обьем {min} грн"))
        return data

    def data_for_xlsx(self):
        data = [[],[],[],[],[],[],[],[],[],[]]
        j = 0
        r = Currency.get_info(self)
        for i in range(10):
            price = round(float(r.get('data')[i].get('adv').get('price')), 2)
            amount = round(float(r.get('data')[i].get('adv').get('surplusAmount')), 2)
            min = round(float(r.get('data')[i].get('adv').get('minSingleTransAmount')), 2)

            data[j].append(price)
            data[j].append(amount)
            data[j].append(min)
            j += 1

        return data


# c = Currency.get_info("UAH", "BUY",['PrivatBank'])
#c = Currency("UAH", "BUY", ['PrivatBank']).data_convert()
#print(c)
# print(Currency.get_info("UAH", "BUY",['PrivatBank']))

# Currency.get_info("UAH", "SELL",['PrivatBank'])
