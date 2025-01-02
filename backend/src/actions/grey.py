from typing import Optional

from src.actions.base import RateProvider
from src.config import GREY_MOBILE_TOKEN


class GreyRateProvider(RateProvider):
    def __init__(self):
        self.url = 'https://user-gw.grey.engineering/v2/currency/USD/rates'
        self.headers = {
            'Authorization': f'Hash {GREY_MOBILE_TOKEN}',
            'X-App-Version': '1.8.6',
            'Accept-Language': 'en',
            'Accept': 'application/json',
            'Accept-Charset': 'UTF-8',
            'User-Agent': 'ktor-client',
            'Content-Type': 'application/json',
            'Connection': 'Keep-Alive',
        }
        self.is_p2p = False

    def get_naira_usd_rate(self) -> Optional[float | int]:
        response = self.make_request(self.url, {}, self.headers, 'GET')
        for data in response:
            if data['code'] == "USD-NGN":
                return data['rate']


if __name__ == "__main__":
    provider = GreyRateProvider()
    dd = provider.get_naira_usd_rate()
    print(dd)
