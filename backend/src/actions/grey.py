from src.actions.base import RateProvider
from src.config import GREY_AUTH_TOKEN

class GreyRateProvider(RateProvider):
    def __init__(self):
        self.url = 'https://user-gw.grey.engineering/v2/currency/USD/rates'
        self.headers = {
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en',
            'authorization': f"Bearer {GREY_AUTH_TOKEN}",
            'origin': 'https://app.grey.co',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }
        self.is_p2p = False


    def get_naira_usd_rate(self):
        response = self.make_request(self.url, {}, self.headers, 'GET')
        data = response
        return data



if __name__ == "__main__":
    provider = GreyRateProvider()
    dd = provider.get_naira_usd_rate()
    print(dd)

