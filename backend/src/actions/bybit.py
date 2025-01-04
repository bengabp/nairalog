from typing import Dict
from src.actions.base import RateProvider, Rate
import pandas as pd


class BybitRateProvider(RateProvider):
    def __init__(self):
        self.url = 'https://api2.bybitglobal.com/fiat/otc/item/online'
        self.headers = {
            'accept': 'application/json',
            'accept-language': 'en',
            'content-type': 'application/json;charset=UTF-8',
            'lang': 'en',
            'origin': 'https://www.bybitglobal.com',
            'platform': 'PC',
            'priority': 'u=1, i',
            'referer': 'https://www.bybitglobal.com/',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }
        self.is_p2p = True
        self.platform_name = "bybit"

    def get_average_price(self, data: Dict) -> float:
        df = pd.DataFrame(data.get('result', {}).get('items', []))
        df[['price', 'minAmount']] = df[['price', 'minAmount']].astype(float)
        df_f = df[df['minAmount'] > 500000]
        price = df_f['price'].mean().round(2).__float__()
        return price

    def get_naira_usd_rate(self) -> Rate:
        rt = {}
        for k,v in {
            "buy_price": 1,
            'sell_price': 0
        }.items():
            json_data = {
                'userId': 149524519,
                'tokenId': 'USDT',
                'currencyId': 'NGN',
                'payment': [
                    '520',
                    '470',
                    '14',
                    '518',
                    '517',
                    '516',
                ],
                'side': str(v),
                'size': '100',
                'page': '1',
                'amount': '1000000',
                'vaMaker': True,
                'bulkMaker': False,
                'canTrade': True,
                'sortType': 'TRADE_PRICE',
                'paymentPeriod': [],
                'itemRegion': 1,
            }
            response = self.make_request(self.url, {}, self.headers, "POST", json_data = json_data)
            rt[k] = self.get_average_price(response)

        rt.update({
            "platform": self.platform_name,
            "is_p2p": self.is_p2p,
        })
        return Rate(**rt)


if __name__ == '__main__':
    bybit_rate = BybitRateProvider()
    bybit_rate.get_naira_usd_rate()
